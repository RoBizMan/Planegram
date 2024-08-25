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

---

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/testing/css_validation/css_jigsaw_validation.png) | Pass: No error found |

---

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/testing/js_validation/script_jshint_validation.png) | All clear, no errors found |

---

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

---

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Sign Up | Login | Sign Out | Grams | Detailed Gram | Upload | Edit Gram | Report Gram | 404 Error | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/chrome/chrome_comp_404.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/firefox/firefox_comp_404.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/edge/edge_comp_404.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_404.png) | Works as expected |

---

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Sign Up | Login | Sign Out | Grams | Detailed Gram | Upload | Edit Gram | Report Gram | 404 Error | 500 Error | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Apple MacMini | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_home.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signup.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_login.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_signout.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_grams.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_detailed_gram.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_upload.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_edit.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_report.png) | ![screenshot](documentation/testing/web_compatibility/safari/safari_comp_404.png) | ![screenshot](documentation/testing/web_compatibility/chrome/pc_500.png) | Works as expected |
| Apple iPad Pro | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_home.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_signup.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_login.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_signout.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_grams.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_detailed_gram.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_upload.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_edit.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_report.png) | ![screenshot](documentation/testing/responsiveness/ipadpro/ipadpro_404.png) | N/A | Works as expected |
| Microsoft Surface Pro 7 | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_home.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_signup.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_login.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_signout.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_grams.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_detailed_gram.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_upload.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_edit.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_report.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_404.png) | ![screenshot](documentation/testing/responsiveness/surfacepro7/surfacepro7_500.png) | Works as expected |
| Google Pixel 7 | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_home.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_signup.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_login.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_signout.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_grams.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_detailed_gram.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_upload.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_edit.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_report.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_404.png) | ![screenshot](documentation/testing/responsiveness/pixel7/pixel7_500.png) | Works as expected |

---

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse/light_home_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_home_desktop.png) | Some minor warnings |
| Sign Up | ![screenshot](documentation/testing/lighthouse/light_signup_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_signup_desktop.png) | Some minor warnings |
| Login | ![screenshot](documentation/testing/lighthouse/light_login_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_login_desktop.png) | Some minor warnings |
| Sign Out | ![screenshot](documentation/testing/lighthouse/light_signout_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_signout_desktop.png) | Some minor warnings |
| Grams | ![screenshot](documentation/testing/lighthouse/light_grams_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_grams_desktop.png) | Some minor warnings. Slow response time due to loading multiples images |
| Detailed Gram | ![screenshot](documentation/testing/lighthouse/light_detailedgram_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_detailedgram_desktop.png) | Some minor warnings. Slow response time due to loading a large image |
| Upload | ![screenshot](documentation/testing/lighthouse/light_upload_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_upload_desktop.png) | Some minor warnings |
| Edit Gram | ![screenshot](documentation/testing/lighthouse/light_editgram_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_editgram_desktop.png) | Some minor warnings |
| Report Gram | ![screenshot](documentation/testing/lighthouse/light_report_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_report_desktop.png) | Some minor warnings |
| 404 Error | ![screenshot](documentation/testing/lighthouse/light_404_mobile.png) | ![screenshot](documentation/testing/lighthouse/light_404_desktop.png) | Some minor warnings |

---

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | The Home page is expected to hide in the navigation bar and redirected a logged user to the Grams page. | Tested the feature by logging in Planegram. | The feature behaved as expected, and it hid the Home page and redirected the logged user to the Grams page. | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | The home page is expected to redirect a logged user to the Grams page when brute-forced the URL of the home page. | Tested the feature by brute-forced the URL of the home page while logged in. | The feature behaved as expected, and it automatically redirected the logged in user to the Grams page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog01.png) |
| Sign Up | | | | | |
| | The Sign Up page is expected to redirect a logged user to the Grams page when brute-forced the URL of the Sign Up page. | Tested the feature by brute-forced the URL of the Sign Up page while logged in. | The feature behaved as expected, and it automatically redirected the logged in user to the Grams page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog02.png) |
| Login | | | | | |
| | The Login page is expected to redirect a logged user to the Grams page when brute-forced the URL of the Login page. | Tested the feature by brute-forced the URL of the Login page while logged in. | The feature behaved as expected, and it automatically redirected the logged in user to the Grams page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog03.png) |
| Sign Out | | | | | |
| | The Sign Out page is expected to redirect a non-logged user or visitor to the Home page when brute-forced the URL of the Sign Out page. | Tested the feature by brute-forced the URL of the Sign Out page while already logged out or being a visitor to the site. | The feature behaved as expected, and it automatically redirected users to the Home page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog04.png) |
| Upload | | | | | |
| | The Upload page is only appeared on the navigation bar when a user is logged in. | Tested the feature by logging in Planegram. | The feature behaved as expected, and it displayed the Upload navigation bar. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog05.png) |
| | The form in the Upload can only submit once all fields are filled in to prevent the empty form from submitting. | Tested the feature by deliberately leave one field and all fields unfilled. | The feature behaved as expected, and it displayed a warning message "Please fill in this field." and would not submit the form. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog06.png) |
| | The Upload page is expected to redirect a non-logged user or visitor to the Login page when brute-forced the URL of the Upload page to prevent unauthorised uploads. | Tested the feature by brute-forced the URL of the Upload page while logged out or being a visitor of the site. | The feature behaved as expected, and it automatically redirected users to the Login page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog07.png) |
| Detailed Gram | | | | | |
| | The Detailed Gram page is expected not to display all buttons, but the Login button to like Gram for a non-logged user or visitor. | Tested the feature by visiting the Detailed Gram page as the logged user, but not the owner of the Gram post. | The feature behaved as expected, and it only displayed the Like/Unlike and Report buttons. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog08.png) |
| | The Detailed Gram page is expected not to display all buttons, but the Like/Unlike and Report buttons for a logged user that is not the user of the Gram post. | Tested the feature by visiting the Detailed Gram page as a non-logged user or visitor. | The feature behaved as expected, and it did not display all buttons, but the Login button. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog09.png) |
| | The Detailed Gram page is expected to immediately reload the same page and display a warning message when the user A attempts to report the same detailed gram more than once to prevent spamming report on the same Detailed Gram post. | Tested the feature by reporting the Gram post for the first time, then reporting the same Gram post multiple times. | The feature behaved as expected, and it immediately reloaded the Detailed Gram page and displayed the warning message "You have already reported this gram." | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog14.png) |
| Edit Gram | | | | | |
| | The Edit Gram page is expected to redirect a non-logged user or visitor to the Login page when brute-forced the URL of the specific Gram post to be edited to prevent unauthorised edit of the Gram post. | Tested the feature by brute-forced the URL of the specific post edit as a non-logged user or visitor of the site. | The feature behaved as expected, and it redirected a non-logged user or visitor to the Login page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog10.png) |
| | The Edit Gram page is expected to immediately redirect the user A back to the Grams page when attempting to brute-force the edit URL of the user B's Detailed Gram and display a warning message to prevent unauthorised user A to edit user B's post. | Tested the feature by brute-forced the edit URL of the user B's Detailed Gram as the user A. | The feature behaved as expected, and it immediately redirected the user A back to the Grams page and displayed the warning message that the user A is not authorised to edit the user B's post. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog11.png) |
| | The Edit Gram page is expected to immediately redirect the logged user B back to the Grams page when attempting to brute-force the edit URL of the user A's Detailed Gram by user B logging in to edit the user A's Gram post and display a warning message to prevent unauthorised user B to edit user A's post. | Tested the feature by brute-forced the edit URL of the user A's Detailed Gram as the user B from being logged out to logged in. | The feature behaved as expected, and it immediately redirected the user B back to the Grams page and displayed the warning message that the user B is not authorised to edit the user A's post. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog12.png) |
| Report Gram | | | | | |
| | The Report Gram page is expected to redirect a non-logged user or visitor to the Login page when brute-forced the URL of the specific Gram post to be reported to prevent unauthorised report of the Detailed Gram post. | Tested the feature by brute-forced the URL of the specific post report as a non-logged user or visitor of the site. | The feature behaved as expected, and it redirected a non-logged user or visitor to the Login page. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog13.png) |
| | The Report Gram page is expected to immediately redirect the user A back to the user B's Detailed Gram page when attempting to brute-force the report URL of the user B's Detailed Gram that have already reported before and display a warning message to prevent user A from spam reporting user B's post. | Tested the feature by brute-forced the report URL of the user B's Detailed Gram as the user A that have already reported the same user B's post. | The feature behaved as expected, and it immediately redirected the user A back to the Grams page and displayed the warning message that the user A have already reported the user B's post. | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog15.png) |
| | The Report Gram page is expected to immediately redirect the logged user A back to the user B's Detailed Gram page and display a warning message that the user A have already reported the User B's post when attempting to brute-force the edit URL of the user B's Detailed Gram by logged-out user A logging in to report the user B's Gram post and display a warning message to prevent spamming report on the same Detailed Gram post. | Tested the feature by brute-forced the report URL of the user B's Detailed Gram as the user A from being logged out to logged in. | The feature behaved as expected, and it immediately redirected the user A back to the Detailed Gram page and displayed the warning message "You have already reported this gram." | Test concluded and passed | ![screenshot](documentation/testing/def_programming/def_prog16.png) |

---

