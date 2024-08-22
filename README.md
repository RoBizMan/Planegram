# [PLANEGRAM](https://planegram-ef1046dc025e.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RoBizMan/Planegram)](https://github.com/RoBizMan/Planegram/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RoBizMan/Planegram)](https://github.com/RoBizMan/Planegram/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RoBizMan/Planegram)](https://github.com/RoBizMan/Planegram)

---

## Introduction

Welcome to Planegram: The Ultimate Hub for Aviation Enthusiasts! If you have a passion for aviation and a love for capturing the beauty of aeroplanes as they soar through the skies, you’ve landed in the right place. Planegram is your premier destination for all things related to aviation photography.

The primary goal of Planegram is to create a vibrant, user-friendly platform that connects aviation enthusiasts and photographers worldwide. By showcasing stunning imagery and providing valuable resources, Planegram aims to inspire a community of individuals who share a love for flight and the art of capturing it.

## Target Audience

Planegram is designed for a diverse audience, including aviation fans, aspiring photographers, and curious travellers. Whether you are a seasoned photographer looking to refine your skills or a newcomer eager to learn about aviation photography, Planegram welcomes you to share your passion and connect with fellow sky enthusiasts. The platform is also ideal for those who appreciate the elegance of flight and want to explore the world of aviation through photography.

## Value Proposition

At Planegram, users can enjoy a streamlined experience focused on aviation photography. The website features a collection of stunning aeroplane images, each accompanied by captions that include the plane's make and model, the name of the photographer, and the number of likes received. This simple yet engaging format allows users to appreciate the artistry of aviation photography while connecting with a community of fellow enthusiasts. 

Join Planegram today and embark on a visual journey through the skies, capturing the essence of flight and discovering the joy of aviation photography together!

![screenshot](documentation/introduction/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://planegram-ef1046dc025e.herokuapp.com)

---

## UX

In this project, I follow the Five Planes of User Experience model invented by Jesse James Garrett.

### Five Planes of User Experience

This model aids in transforming from abstract ideas, such as creating objectives of the project and identifying the user needs, to concrete concepts, such as assembling visual elements together to produce the visual design of the idea to meet the project's objectives and users' needs.

#### The Strategy Plane
The vision for Planegram is to be a unique, visually engaging platform where aviation enthusiasts and photographers can share and appreciate stunning images of aeroplanes. Unlike other platforms, Planegram focuses on building a visually appealing and engaging space for aviation lovers to showcase their passion through photography with minimal complexity.

##### Business Goals:
•	Community Engagement: Foster a community of aviation enthusiasts who actively share their aviation photos and engage by liking the images of others. We value your input and aim to shape Planegram based on your needs and preferences.
•	Content Creation: Foster a dynamic and engaging feed, continuously enriched by high-quality aviation images uploaded by our users.
•	Brand Identity: The go-to platform for aviation photography, renowned for its intuitive, user-friendly interface and captivating visual content.

##### User Needs:
•	Aviation Enthusiasts and Photographers: A visually driven platform that allows them to upload and share aviation photos with others who share their passion.
•	Casual Users: A simple, easy-to-use platform where they can browse beautiful images of planes and engage with the content by liking their favourites.
•	Simplicity Seekers: Users prefer a straightforward experience without the complexity of comments, advanced search, or additional features like monetisation.
In this simplified context, the core value of Planegram lies in providing a streamlined experience focused on visual content and community engagement through photo sharing and likes.

#### Scope Plane

Based on the main objective and goals set out in the Strategy Plane, these requirements for developing the website are broken down into two categories:

##### Functional Requirements:
•	User Accounts and Profiles: Users should be able to create an account, set up a basic profile, and upload their aviation photos.
•	Image Upload and Sharing: A simple process for users to upload their images, add essential captions (e.g., plane make and model), and share them on the platform.
•	Like Feature: Users should be able to like photos, with the total number of likes displayed alongside the image.
•	Feed Display: A visual feed displaying photos in a grid format, similar to Instagram, where users can scroll through images of planes shared by the community.
•	Primary Navigation: Users should be able to navigate between their profile, the main photo feed, and liked images.

##### Content Requirements:
•	Aviation Photo Gallery: A visually organised gallery showcasing user-uploaded photos, with each image displaying the plane's make and model, the photographer’s name, and the number of likes.
•	User Profiles: Basic profiles showing the user's uploaded photos, a brief bio, and their total number of likes received.
•	Curated Content: A selection of standout photos or featured users could be highlighted to encourage higher engagement and showcase quality content.

#### The Structure Plane

The requirements outlined in the Scope Plane were then used to create a structure for the website. A site map below shows how users can navigate the website easily.

"Image here"

#### The Skeleton Plane

Please refer to the [Wireframes](#Wireframes) section for more detailed wireframing.

#### The Surface Plane

[Click here to view the live site.](https://planegram-ef1046dc025e.herokuapp.com)

### Colour Scheme

I used [Color Hunt](https://colorhunt.co/palette/f8f9fa380788ffc106212529#justCreated) to generate my colour palette.

![screenshot](documentation/ux/colour_palette.png)

- `#F8F9FA` used for primary background and text colour.
- `#380788` used for primary navbar, container, and footer colour.
- `#FFC106` used for secondary button and highlight links colour.
- `#212529` used for secondary text.

The colour palette represents a plane soaring above the night sky during a red-eye flight. However, the colour palette needed to pass the minimum colour contrast set by the Web Content Accessibility Guide (WCAG). The colour palette was tested using [Coolors' Color Contrast Checker](https://coolors.co/contrast-checker/). The result below shows that these colours passed the minimum WCAG contrast ratio.

<details>
<summary>Color Contrast Checker</summary>

![screenshot](documentation/ux/black_gold.png)
![screenshot](documentation/ux/gold_navy.png)
![screenshot](documentation/ux/white_navy.png)
</details>

<br>

### Typography

- [Bootstrap's native font stack](https://getbootstrap.com/docs/5.3/content/reboot/#native-font-stack) was used throughout the site.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer and buttons in a detailed gram view.

---

## User Stories

### New Site Users

- As a new site user, I would like to create an account, so that I can start sharing my aviation photos with the Planegram community.
- As a new site user, I would like to upload my first aviation photo, so that I can contribute to the platform and share my passion for airplanes.
- As a new site user, I would like to browse the photo feed, so that I can see aviation photos uploaded by others and enjoy the community's content.
- As a new site user, I would like to like photos, so that I can engage with the content that resonates with me.
- As a new site user, I would like to see the number of likes on each photo, so that I can gauge which images are popular in the community.

### Returning Site Users

- As a returning site user, I would like to upload new aviation photos, so that I can continue contributing to the Planegram community.
- As a returning site user, I would like to browse the latest photos on the platform, so that I can keep up with new content from other aviation enthusiasts.
- As a returning site user, I would like to like additional photos, so that I can continue engaging with the content that I enjoy.
- As a returning site user, I would like to edit the captions or details of my previously uploaded photos, so that I can update or improve the information shared with the community.
- As a returning site user, I would like to delete my previously uploaded photos, so that I can remove any content that no longer represents my best work or that I no longer want to share.

### Site Admin

- As a site administrator, I should be able to monitor reports submitted by users, so that I can address any incorrect information or inappropriate content on the platform.
- As a site administrator, I should be able to remove or correct any reported photos, so that the platform maintains accurate and appropriate content.
- As a site administrator, I should be able to monitor the overall content quality, so that I can ensure the platform aligns with the community's standards and values.

---

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/mobile/mobile_homepage.png)

Sign Up
- ![screenshot](documentation/wireframes/mobile/mobile_signup.png)

Login
- ![screenshot](documentation/wireframes/mobile/mobile_login.png)

Sign Out
- ![screenshot](documentation/wireframes/mobile/mobile_signout.png)

Upload
- ![screenshot](documentation/wireframes/mobile/mobile_upload.png)

Edit
- ![screenshot](documentation/wireframes/mobile/mobile_edit.png)

Report
- ![screenshot](documentation/wireframes/mobile/mobile_report.png)

Grams
- ![screenshot](documentation/wireframes/mobile/mobile_grams.png)

Detailed Gram
- ![screenshot](documentation/wireframes/mobile/mobile_detailedgram.png)

</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/tablet/tablet_homepage.png)

Sign Up
- ![screenshot](documentation/wireframes/tablet/tablet_signup.png)

Login
- ![screenshot](documentation/wireframes/tablet/tablet_login.png)

Sign Out
- ![screenshot](documentation/wireframes/tablet/tablet_signout.png)

Upload
- ![screenshot](documentation/wireframes/tablet/tablet_upload.png)

Edit
- ![screenshot](documentation/wireframes/tablet/tablet_edit.png)

Report
- ![screenshot](documentation/wireframes/tablet/tablet_report.png)

Grams
- ![screenshot](documentation/wireframes/tablet/tablet_grams.png)

Detailed Gram
- ![screenshot](documentation/wireframes/tablet/tablet_detailedgram.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/desktop/desktop_homepage.png)

Sign Up
- ![screenshot](documentation/wireframes/desktop/desktop_signup.png)

Login
- ![screenshot](documentation/wireframes/desktop/desktop_login.png)

Sign Out
- ![screenshot](documentation/wireframes/desktop/desktop_signout.png)

Upload
- ![screenshot](documentation/wireframes/desktop/desktop_upload.png)

Edit
- ![screenshot](documentation/wireframes/desktop/desktop_edit.png)

Report
- ![screenshot](documentation/wireframes/desktop/desktop_report.png)

Grams
- ![screenshot](documentation/wireframes/desktop/desktop_grams.png)

Detailed Gram
- ![screenshot](documentation/wireframes/desktop/desktop_detailedgram.png)

</details>

---

