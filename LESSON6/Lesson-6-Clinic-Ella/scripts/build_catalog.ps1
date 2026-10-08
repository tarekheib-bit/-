# Build Catalog Script - PowerShell version
# Creates catalog of all files with hashes and tentative categories

param(
    [string]$ArchiveRoot = "."
)

function Get-FileHash256 {
    param([string]$FilePath)
    $hasher = [System.Security.Cryptography.SHA256]::Create()
    $stream = [System.IO.File]::OpenRead($FilePath)
    $hash = $hasher.ComputeHash($stream)
    $stream.Close()
    return [BitConverter]::ToString($hash) -replace '-'
}

function Categorize-File {
    param([string]$FileName)

    $nameLower = $FileName.ToLower()

    # Accounting
    if ($nameLower -match 'חשבונ|תשלום|הנהלה|בנק|הוצאה|הכנסה|שכר|תזרים|מחיר|חשבו') {
        return 'הנהלת-חשבונות'
    }

    # Credit
    if ($nameLower -match 'אשראי|הלוואה|כרטיס') {
        return 'בנקאות-ואשראי'
    }

    # HR
    if ($nameLower -match 'שכר|עובד|צוות|העסקה') {
        return 'שכר-ומשאבי-אנוש'
    }

    # Sales/CRM
    if ($nameLower -match 'לקוח|מכירה|חבילה|כרטסת|ספק|קשר') {
        return 'מכירות-ולקוחות-CRM'
    }

    # Marketing
    if ($nameLower -match 'לוגו|מיתוג|צבע|פונט|שיווק|קמפיין|פלייר|ניוזלטר|תמונה') {
        return 'שיווק-ומותג'
    }

    # Operations
    if ($nameLower -match 'מלאי|הנהלה|תהליך|נוהל|מפעיל') {
        return 'תפעול-ERP'
    }

    # Legal
    if ($nameLower -match 'חוזה|הסכם|משפט|הסכמה|מדיניות|תנאים') {
        return 'משפטי-וחוזים'
    }

    # Digital
    if ($nameLower -match 'קישור|אתר|דומיין|דיגיטל|אינטרנט') {
        return 'דיגיטל-ולינקים'
    }

    # Reviews
    if ($nameLower -match 'ביקור|דירוג|המלצה|ביקורת') {
        return 'תקשורת-וביקורות'
    }

    return 'לא-מסווג'
}

# Build catalog
$backupDir = Join-Path $ArchiveRoot "00-מקור-גולמי"
$aiReadyDir = Join-Path $ArchiveRoot "02-AI-ready"
New-Item -ItemType Directory -Path $aiReadyDir -Force | Out-Null

$catalog = @{
    metadata = @{
        archive_root = $ArchiveRoot
        total_files = 0
        categories = @{}
    }
    files = @()
}

$categoryCount = @{}
$typeCount = @{}

Write-Host "`n📋 Building catalog..."

Get-ChildItem -Path $backupDir -Recurse -Force | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
    try {
        $ext = $_.Extension.TrimStart('.').ToLower()
        $category = Categorize-File $_.Name

        $relPath = $_.FullName.Substring($backupDir.Length + 1)

        $hash = Get-FileHash256 $_.FullName

        $entry = @{
            path = $relPath
            filename = $_.Name
            size = $_.Length
            hash = $hash
            category = $category
            type = if ($ext) { $ext } else { "no-extension" }
        }

        $catalog.files += $entry

        # Count by category
        if ($categoryCount.ContainsKey($category)) {
            $categoryCount[$category]++
        } else {
            $categoryCount[$category] = 1
        }

        # Count by type
        if ($typeCount.ContainsKey($ext)) {
            $typeCount[$ext]++
        } else {
            $typeCount[$ext] = 1
        }
    } catch {
        Write-Host "⚠ Warning: Could not process $($_.FullName): $_"
    }
}

$catalog.metadata.total_files = $catalog.files.Count
$catalog.metadata.categories = $categoryCount

# Save catalog
$catalogPath = Join-Path $aiReadyDir "catalog.json"
$catalogJson = $catalog | ConvertTo-Json -Depth 10
[System.IO.File]::WriteAllText($catalogPath, $catalogJson, [System.Text.Encoding]::UTF8)

# Print summary
Write-Host "`n" + "="*60
Write-Host "✓ CATALOG SUMMARY"
Write-Host "="*60
Write-Host "Total files: $($catalog.files.Count)`n"

Write-Host "📂 Categories:"
$categoryCount.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
    $status = if ($_.Key -eq "לא-מסווג") { "?" } else { "✓" }
    Write-Host "  $status $($_.Key): $($_.Value)"
}

Write-Host "`n📄 Top file types:"
$typeCount.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 10 | ForEach-Object {
    Write-Host "  .$($_.Key): $($_.Value)"
}

Write-Host "`n✓ Catalog saved to: $catalogPath"
Write-Host "="*60
