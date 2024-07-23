## Introduction 
CyberSecurity Mindset
Welcome to Cybersecurity Mindset blog! Here, you'll find the latest insights, tips, and news to help you stay safe in the digital world. Whether you're a seasoned professional or just starting your journey in cybersecurity, our content is designed to inform and empower you. Join us as we explore the ever-evolving landscape of cyber threats and defenses. Stay informed, stay secure!

Our focus and goal is to provide comprehensive and up-to-date information on a wide range of cybersecurity topics






## Table of contents
  - Introduction
  - Overview
  - UX - User Experience
   - Structural plane
  - Design Aesthetic
    - Colour Scheme
    - Typography
    - Visual Elements

- Project planning 
  - Agile methodology project Management with Github 
     - Repositories
     - Issues and story points allocation 
     - MoSCoW Prioritisation 
     - Project Boards
     - milestones
     - user stories
     - Epics
- Scope plan
- Skeleton and surface 
    - wireframes
- Database Schema
   - Entity Relationship Diagram
   - ERD Table overview
   - Relationships
- Security
   - Data Encryption
   - CSRF Tokens
   - AllAuth
- Features
   - Existing features
   - functionality
   - CRUD Functionality
- Featue remaining to implement
- Technologies Used
-   fontend
-  backend
-  deployment
-   version control
-   development tools
-  libraries and frameworks
-   validation tools
- Testing
- Cloning and Forking
- Credits         
     

## Overview 
Here's an overview of what you can expect:

1. Latest News and Trends: Stay informed about the latest developments in the world of cybersecurity. We cover breaking news, emerging threats, and the latest trends affecting the digital landscape.

2. Expert Insights: Gain valuable knowledge from industry experts. Our blog features articles, interviews, and opinion pieces from seasoned cybersecurity professionals.

3. Practical Tips and Guides: Learn how to protect yourself and your organization from cyber threats. We provide practical advice, step-by-step guides, and best practices for enhancing your security posture.

4. Threat Analysis: Understand the nature of various cyber threats. We delve into different types of attacks, their methodologies, and how to defend against them.

5. Product Reviews and Recommendations: Find reviews and recommendations for cybersecurity tools and software. We evaluate the latest products to help you make informed decisions.

6. Case Studies: Read real-world examples of cybersecurity incidents and their resolutions. These case studies offer insights into how organizations respond to and recover from cyberattacks.

7. Regulatory Updates: Keep up with changes in cybersecurity regulations and compliance requirements. We provide updates on relevant laws and standards that impact businesses and individuals.

8. Community Engagement: Join our community of cybersecurity enthusiasts. Engage in discussions, share your experiences, and connect with like-minded individuals.

We are committed to delivering high-quality content that educates, informs, and empowers our readers. Thank you for visiting, and we hope you find our blog both useful and engaging. Stay safe and secure!


## UX - User Experience
The US design of Cybersecurity Mindset blog is a balance between an engaging, user-friendly interface and ensuring security best practices. Here's the UX design outline:
## Structural plane
### 1. Homepage

Header:
- The Logo is at the Top left corner.
- Followed by the Navigation Menu: Home, Categories, About, Contact, Search (magnifying glass icon).
- The Signup/Login page is at Top right corner.
- The Create-post and Log-out is seen when a user has logged in, this allowers access to only login users.

Hero Section:
- The Featured Articles Slider Highlights the latest or most important posts.
- The Search Bar is Prominent and centrally located for easy access.

Main Content:
- Shows a list view of recent Blog_posts with authors, titles, excerpts, publication dates and time.
- The read_more link takes user to the detailed articles for each blog_post

Footer:
- There are Quick Links to important pages.
- There are Social Media Link  Icons to my social media profiles.


 ### 2. Blog Post Page

Article Content:
- Title and Author Information: Displays the title and author's name.
- The Images: An image to compliment each blog post.
- Content Area: There is a Clean, readable font with ample spacing.
- Related Articles: Suggested reads based on the current post.
- publication date and time comes directly after the detailed article.
- Comment Section: Is Secured and moderated with the option for users to login to comment, update and delete their comments.



### 3. Categories Page

- Category Header: Clear title and brief description of the category.
- Article List: Similar layout to the homepage with thumbnails and excerpts.
- Pagination: For navigating through older posts.

### 4. About Page

- Mission Statement: The About page Briefly explains the blog’s purpose.
- Team Members: Display Photos of contributors.

### 5. Contact Page

- Contact Form: The Django Secure form is used for inquiries.
- A confirmation message is seen after the user has successfully sent out an inquiry.


### 6. Additional Features

Responsive Design:
- A responsive design is used to Ensure the site is fully functional and visually appealing on all devices, from desktops to smartphones, thanks to Django.

Accessibility:
- The site is accessible to users with disabilities, complying with WCAG standard.

## Design Aesthetic
- Color Scheme: A Professional and clean shades of blue, gray, and white to convey trust and security.
- Typography: There is a Clear and readable fonts, with a good contrast against the background.
- Visual Elements: relevant and high-quality images is used to enhance content.

## Project planning
## Agile methodology project Management with Github 
CyberSecurity Mindset adopted the Agile methodology project Management with GitHub using GitHub's features which emphasize flexibility, collaboration, and iterative progress. Here's a comprehensive explanation of some of the features i used for the Cybersecurity Mindset blog to manage an agile project using GitHub:

### 1. Repositories

- Central Hub: Each project is stored in a GitHub repository, serving as the central hub for all project-related code, documentation, and resources.
- Version Control: GitHub provides version control, allowing teams to track changes, revert to previous versions, and collaborate efficiently on code.

### 2. Issues and story points allocation

- Task Tracking:  Issues in GitHub were used to track tasks, bugs, enhancements, and user stories. Each issue represents a piece of work that needs to be completed.
- Labels: labels are used to categorize issues by type (e.g., must have, could have, should have), priority, status (e.g., in-progress, done), and sprint.
- Assignees: Assign issues to team members to designate responsibility, in this project, it was only myself.

### 3. MoSCoW Prioritization 

1. Must have (M): These are critical requirements or tasks that are essential for the success of the project. Without these, the project would fail or be significantly compromised.

2. Should have (S): Important requirements or tasks that are not critical but have a high value. They are not absolutely necessary for the current project phase but should be included if possible.

3. Could have (C): Desirable requirements or tasks that would be beneficial if included but are not necessary. They can be deferred or dropped if time or resources are limited.

4. Won't have (W): These are the least critical requirements or tasks that will not be included in the current project phase but might be considered for future phases.

### 4. Project Boards 

- Kanban Boards: GitHub Projects provide kanban-style boards where issues can be organized into columns such as To Do, In Progress, and Done. This visualizes the workflow and progress of tasks.

### 5. Milestones

- Sprint Planning: milestones were used to represent sprints or releases. Each milestone had a due date and a collection of issues that need to be completed within the sprint even though there was room for adjustment, not fixed or sequencial.
- Progress Tracking: The progress of milestones were tracked by monitoring the number of completed issues versus the total number of issues.

- README: Each repository typically has a README file that provides an overview of the project, setup instructions, and other important information.

## user stories

User stories are a fundamental element of Agile development, focusing on the needs and experiences of end-users. They are short, simple descriptions of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. Here is the link to the Cybersecurity Mindset user stories...

## Epics

An epic in Agile methodology is a large body of work that can be broken down into smaller tasks or user stories. Epics often span multiple sprints and sometimes even projects, providing a high-level view of significant features or functionalities. Here's a detailed overview of epics

## Scope plan

- *Purpose*: Cybersecurity Mindset aims to educate and raise awareness about cybersecurity threats, best practices, and technologies. Also aims to provide updates on the latest cybersecurity trends, news, and incidents as well as to share knowledge and help others develop their skills in cybersecurity.

### Target 

Audience Cybersecurity professionals, IT teams, tech-savvy readers General public, businesses, students, and professionals.

### Goal 
1. Increase the general public’s understanding of cybersecurity threats and best practices.
2. Keep readers informed about the latest developments, trends, and news in cybersecurity.
3. Create a space for like-minded individuals to connect, share knowledge, and discuss cybersecurity topics.
4. Provide resources and guidance for individuals seeking to advance their careers in cybersecurity.
5. Share knowledge and help others develop their skills in cybersecurity etc.


### User Needs
1. Access to update on the latest cybersecurity threats, trends, and news.
2. Ability to understand and implement cybersecurity best practices for personal or organizational security.
3. To advance their careers in cybersecurity through continuous learning and skill development.

## Skeleton and surface 
### Wireframes
Figma was used to design the Cybersecurity Mindset

Home page Wireframe

Read more wireframe

About page Wireframe

Contact page Wireframe

## Database Schema



