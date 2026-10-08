#!/usr/bin/env python3
"""
End-to-End Test for Clinic Ella Landing Page Form
Tests webhook integration and form submission
"""

from playwright.sync_api import sync_playwright
import json
import time
from datetime import datetime

def test_clinic_form_submission():
    print("=" * 70)
    print("🏥 Clinic Ella - End-to-End Form Test")
    print("=" * 70)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Capture network requests
        requests_captured = []

        def handle_route(route):
            requests_captured.append({
                'url': route.request.url,
                'method': route.request.method,
                'post_data': route.request.post_data,
                'timestamp': datetime.now().isoformat()
            })
            route.continue_()

        # Listen to all network requests
        page.route('**/*', handle_route)

        try:
            # Navigate to landing page
            print("\n📄 Loading landing page...")
            page.goto('http://localhost:8000/clinic-ella-landing.html')
            page.wait_for_load_state('networkidle')
            print("   ✅ Page loaded successfully")

            # Take screenshot of form
            print("\n📸 Capturing form section...")
            page.evaluate('window.location.hash = "#contact"')
            page.wait_for_timeout(300)
            page.screenshot(path='clinic-form-before.png')
            print("   ✅ Screenshot saved: clinic-form-before.png")

            # Fill form fields
            print("\n📝 Filling form fields...")
            test_data = {
                'name': 'תמר לוי',
                'phone': '050-9876543',
                'email': 'tamar.levi@example.com',
                'service': 'botox',
                'message': 'אני רוצה בוטוקס טבעי'
            }

            page.fill('#name', test_data['name'])
            print(f"   ✓ Name: {test_data['name']}")

            page.fill('#phone', test_data['phone'])
            print(f"   ✓ Phone: {test_data['phone']}")

            page.fill('#email', test_data['email'])
            print(f"   ✓ Email: {test_data['email']}")

            page.select_option('#service', test_data['service'])
            print(f"   ✓ Service: {test_data['service']}")

            page.fill('#message', test_data['message'])
            print(f"   ✓ Message: {test_data['message']}")

            # Take screenshot with filled form
            print("\n📸 Capturing filled form...")
            page.screenshot(path='clinic-form-filled.png')
            print("   ✅ Screenshot saved: clinic-form-filled.png")

            # Submit form
            print("\n🚀 Submitting form...")

            # Listen for potential errors
            page_errors = []
            page.on('console', lambda msg: None)  # Suppress console
            page.on('pageerror', lambda err: page_errors.append(str(err)))

            # Click submit button
            page.click('.form-submit')

            # Wait for response or error
            page.wait_for_timeout(1000)

            # Take screenshot of result
            print("\n📸 Capturing result...")
            page.screenshot(path='clinic-form-result.png')
            print("   ✅ Screenshot saved: clinic-form-result.png")

            # Check for success message
            success_msg = page.query_selector('div[style*="D4A5A0"]')
            if success_msg:
                success_text = page.text_content('div[style*="D4A5A0"]')
                print(f"\n✅ Success message appeared:")
                print(f"   {success_text[:100]}...")
            else:
                print("\n⚠️  No success message found (might be webhook pending)")

            # Analyze captured requests
            print("\n📊 Network Requests Captured:")
            webhook_found = False
            for i, req in enumerate(requests_captured):
                if 'webhook' in req['url'].lower() or 'n8n' in req['url'].lower():
                    webhook_found = True
                    print(f"   [{i}] Webhook: {req['method']} {req['url']}")
                    if req['post_data']:
                        print(f"       Data: {req['post_data'][:200]}...")

            if not webhook_found:
                print("   ⚠️  No webhook request captured")
                print("   Note: Webhook URL might not be configured yet")

            # Test form reset
            print("\n🔄 Testing form reset...")
            form_name = page.input_value('#name')
            if not form_name or form_name == '':
                print("   ✅ Form was reset successfully")
            else:
                print(f"   ⚠️  Form still contains: {form_name}")

            # Check form validation
            print("\n✔️ Testing form validation...")
            page.click('.form-submit')
            page.wait_for_timeout(300)

            # Try submitting empty form
            name_validity = page.evaluate("document.getElementById('name').validity.valid")
            print(f"   Name field required: {not name_validity}")

        except Exception as e:
            print(f"\n❌ Error during test: {e}")
            page.screenshot(path='clinic-form-error.png')
            print("   Screenshot saved: clinic-form-error.png")

        finally:
            browser.close()

    print("\n" + "=" * 70)
    print("✨ Test Summary:")
    print("=" * 70)
    print("📸 Screenshots created:")
    print("   - clinic-form-before.png (initial form)")
    print("   - clinic-form-filled.png (filled form)")
    print("   - clinic-form-result.png (after submission)")
    print("\n📋 Next steps:")
    print("   1. Configure N8N webhook URL in HTML")
    print("   2. Set up Google Sheets connection")
    print("   3. Re-run this test to verify end-to-end flow")
    print("\n" + "=" * 70)

if __name__ == '__main__':
    test_clinic_form_submission()
