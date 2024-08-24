# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/html_validation/homepage_html_validation.png) | Pass: No error found |
| Login | ![screenshot](documentation/testing/html_validation/signin_html_validation.png) | Pass: No error found |
| Sign Up | ![screenshot](documentation/testing/html_validation/signup_html_validation.png) | 4 errors |
| Sign Out | ![screenshot](documentation/testing/html_validation/signout_html_validation.png) | Pass: No error found |
| Grams | ![screenshot](documentation/testing/html_validation/grams_html_validation.png) | Pass: No error found |
| Detailed Gram | ![screenshot](documentation/testing/html_validation/grams_6_html_validation.png) | Pass: No error found |
| Edit Gram | ![screenshot](documentation/testing/html_validation/grams_8_edit_html_validation.png) | Pass: No error found |
| Like/Unlike Gram | ![screenshot](documentation/testing/html_validation/grams_6_unlike_html_validation.png) | Pass: No error found |
| Upload | ![screenshot](documentation/testing/html_validation/upload_html_validation.png) | Pass: No error found |
| Report | ![screenshot](documentation/testing/html_validation/grams_report_html_validation.png) | Pass: No error found |
| Error 404 | ![screenshot](documentation/testing/html_validation/404_error_html_validation.png) | Pass: No error found |
| Error 500 | ![screenshot](documentation/testing/html_validation/500_error_html_validation.png) | Pass: No error found |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/testing/css_validation/css_jigsaw_validation.png) | Pass: No error found |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/testing/js_validation/script_jshint_validation.png) | All clear, no errors found |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| blog | models.py | ![screenshot](documentation/testing/python_validation/blog_models_ci_linter.png) | All clear, no errors found |
| blog | urls.py | ![screenshot](documentation/testing/python_validation/blog_urls_ci_linter.png) | All clear, no errors found |
| blog | views.py | ![screenshot](documentation/testing/python_validation/blog_views_ci_linter.png) | All clear, no errors found |
| grams | forms.py | ![screenshot](documentation/testing/python_validation/grams_forms_ci_linter.png) | All clear, no errors found |
| grams | urls.py | ![screenshot](documentation/testing/python_validation/grams_urls_ci_linter.png) | All clear, no errors found |
| grams | views.py | ![screenshot](documentation/testing/python_validation/grams_views_ci_linter.png) | All clear, no errors found |
| planegram | urls.py | ![screenshot](documentation/testing/python_validation/planegram_urls_linter.png) | All clear, no errors found |
| planegram | views.py | ![screenshot](documentation/testing/python_validation/planegram_views_linter.png) | All clear, no errors found |
| upload | forms.py | ![screenshot](documentation/testing/python_validation/upload_forms_ci_linter.png) | All clear, no errors found |
| upload | urls.py | ![screenshot](documentation/testing/python_validation/upload_urls_ci_linter.png) | All clear, no errors found |
| upload | views.py | ![screenshot](documentation/testing/python_validation/upload_views_ci_linter.png) | All clear, no errors found |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Sign Up | Login | Sign Out | Grams | Detailed Gram | Upload | Edit Gram | Report Gram | 404 Error | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_404.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_404.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_404.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_404.png) | Works as expected |

