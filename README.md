<div align="center">
<img src="https://github.com/tdignan87/traceVMS/blob/master/static/img/TraceSense_RGB.jpg" target="_blank" rel=""/>
</div>
<div align="center">
<h1>TraceSense - Traceability Company</h1>
</div>

## Introduction

Tracesense is an application used for conducting GMP(good manufacturing practice) audits electronically. Tracesense will allow the user to complete the audit via a tablet, phone, or PC and there is no installation required.<br>

<strong>Tracesense software provides insight and visibility to help raise quality and safety standards across an organisation.</strong> 

Tracesense will record your non compliant items and email them to a specific recipient list at your request to action. 

The benefits of using our software is that it's lightweight, simple to set up and helps eliminate paperwork which has an environmental benefit, but also helps with food compliance. Our software is not over priced and developed by a developer who has over 10 years experience in the food manufacturing industry.

Tracesense is my own company i created in November 2019 and decided to go with that name for the software although this application purely created for educational purposes at this stage.

## Table of Contents
1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stores)
    - [Business Goals](#business-goals)
    - [Developer Goals](#developer-goals)
    - [User Requirements & Expectations](#customer-stories)
        - [Design Choices](#design-choices)
    - [WireFrames](#wireframes)
    - [Flow Chart](#flowchart)
    

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left To Implement](#features-left-to-implement)


3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    - [Collections Data Structure](#collections-data-structure)
   

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6.[Bugs](#Bugs)

7. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

8. [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

9. [Contact](#contact)

10. [Disclamer](#disclamer)

11. [Access Credentials](#access-credentials)
  

----


# UX

## Project Goals
The goal of this software is to create a responsive, suitable, and fully functional application for completing food safety auditing tasks. The software is aimed at food manufacturers
specifically designed so they can complete GMP audits easily without having to record it on paper and then update an excel document at a later stage.

The selling point for this software will be ease of use and removal of paper from the process. In the future the aim is to have lots of traceability data capturing functionality to allow companies to remove the majority of paperwork from there processes.

## User Stories:
User goals are:

- Ability to try the products before purchasing to ensure it's suitable for my needs.

- Ability to purchase the product easily to unlock the full functionality.

- Ease of use across any of my devices.

- Secure so my data is not easily accessible by other parties.

- Confidence in the system so it allows us to comply with food safety while removing paperwork from our processes. 

## Business Goals
- An app that's fit for purpose and generates revenue for the business.

- An app that is welcoming to the user, informative and explains why it is beneficial to them.

- Emphasis on helping the customer achieve paperless compliance, and highlight that the developer has experience first hand working in a food manufacturing environment.

The target businesses to use this application are:

## Developer Goals

Developer goals are:

- Learning about MVT's (similar to MVC) and how to build full stack applications.

- Learning about deploying full applications to heroku.

- Future goal is to use this as part of an actual business.

- Fit for purpose app which users will definately see as a benefit to there business.

## Design Choices

The following design choices were made:

### Fonts

* Google Font [Fira Sans](https://fonts.google.com/specimen/Fira+Sans) was chosen as it looks great across multiple interfaces.

### Colours

* The colours for this project were choosen based on the two primary colours in my company logo. These colours are

- ![#0069A8](https://via.placeholder.com/15/0069A8/000000?text=+) `#0069A8`
- ![#42BFE0](https://via.placeholder.com/15/42BFE0/000000?text=+) `#42BFE0`

## Wireframes

The wireframes were created using [Balsamiq](https://balsamiq.com/) during the scope part of the design and planning process for this project. I found Balsamiq very useful for helping me plan out exactly what i needed for my application to come together.


#### Browser
- [Browser Main Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-main-page.png)
- [Browser Sign Up](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-sign-up.png)
- [Browser Audit Start](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-audit-start.png)
- [Browser Completed Actions](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-completed-actions.png)
- [Browser Configuration](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-config-page.png)
- [Browser Delete Audits](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-delete-audits.png)
- [Browser Departments](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-departments-page.png)
- [Browser Email Panel](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-email-panel.png)
- [Browser Outstanding Actions](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-outstanding-actions.png)
- [Browser Sign In](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-sign-in.png)
#### Mobile
- [Mobile Audit Start ](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-audit-start.png)
- [Mobile Completed Actions](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-completed-actions.png)
- [Mobile Configuration Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-config-page.png)
- [Mobile Delete Audits](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-delete-audits.png)
- [Mobile Departments](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-departments.png)
- [Mobile Email Panel](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-email-panel.png)
- [Mobile Main Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-main-page.png)
- [Mobile Outstanding Tasks](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-outstanding-tasks.png)
- [Mobile Sign In](https://github.com/tdignan87/TraceSense/blob/master/wireframes/mobile-sign-in-page.png)
#### Tablet
- [Tablet Audit Start](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-audit-start.png)
- [Tablet Completed Actions](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-completed-actions.png)
- [Tablet Configuration Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-config-page.png)
- [Tablet Delete Audit](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-delete-audit.png)
- [Tablet Departments Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-departments-page.png)
- [Tablet Email Panel](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-email-panel.png)
- [Tablet Home Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-home-page.png)
- [Tablet Outstanding Actions](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-outstanding-actions.png)
- [Tablet Sign In](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-sign-in.png)
- [Tablet Sign Up](https://github.com/tdignan87/TraceSense/blob/master/wireframes/tablet-sign-up.png)



To go to the main wireframes page please click [this](https://github.com/tdignan87/TraceSense/tree/master/wireframes) link.



## Flow Chart

Please see below a process flow chart of how users will use the application.

<div align="center">
<img src="https://github.com/tdignan87/TraceSense/blob/master/wireframes/flowcharts/ts-user-process-flow.jpg" target="_blank" rel=""/>
</div>


# Features

## Existing Features

### Features on every Page:

- Navbar
    - The navigation bar features the TraceSense company logo..
    - For users using the app there is a list of navbar options available regardless of the page loaded. These are:
    1. Products
    2. Support
    3. Pricing

### Features on main Page:
To Be Completed

## Features left to Implement

1. Start Up Inspection Checks<br>
Ability to create start up check safety questions prior to production runs starting.

2. Stock Receive Checks<br>
Create questions for booking in stock at site, if any stock item does not satisfy booking in quality requirements then user records in the app and email is sent to QA notifying them
that goods have failed the goods inbound checks.

3. Recipes<br>
Store recipe information and costing in the app which can be accessed at any time.

4. Commodities<br>
Store commodity information and suppliers in the app such as sugars, butter etc and which is the supplier.

5. Hygiene Records<br>
Complete hygiene record inspection checks in the app to remove paperwork from there processes.

6. Maintenance Request Form<br>
User can create a maintenance request (form) which will be emailed to the maintenance department for them to acknowledge and complete the request.

7. Quality Assurance Non Conformance Log<br>
In the App it would be great if during production quality assurance personnel can log non conforming issues in the system. They select what product is running, and record non-conforming details for that product. 

8. Dashboard <br>
A dashboard where user can see at a first glance what actions are outstanding, how many audits completed in the last week, month, year, etc.


# Information Architecture

[MySQL](https://www.mysql.com/) was the database choice for my project. An relational database management system was the most appropriate database choice for this project. 


Typical types of data stored in the database are

- Id
- Int
- String
- Boolean
- DateTime

Tracesense relies on the following data structure in addition to the django default authentication tables:

TBL_GMP_QUESTIONS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
GMP_QUESTIONID | Integer | unique | Yes| No |
QUESTION | VarCar(255) | text | No| No |
CREATED | DateTime | DateTime | No| No |
DELETED | bool | bool | No | Yes |



TBL_GMP_ANSWERS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
GMP_ID | Integer | unique | Yes | No |
GMP_QUESTIONID | int | unique | No | No |
ANSWER_CORRECT | VarChar(30)| text | No | Yes |
ANSWER_INCORRECT | VarChar(255) | text| No | Yes |
USERID| int| unique| int | No |
STAMP| DateTime| DateTime| No | No |
IMAGE| Blob|Image| No |Yes |


USERS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
USERID| Integer | unique | Yes | No |
CODE| VarChar(30)| string | No | No |
NAME| VarChar(255)| string| No | No |
PASSWD| VarChar(30)| string| No| No |
TRUSTED_SUPERVISOR| Bool| Bool| No | No |

ALERTUSRS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
ALERTID| Integer | unique | Yes | No |
NAME| VarChar(30)| string | No | No |
EMAIL| VarChar(255)| string| No | No |
DEPARTMENTID| Integer| unique| No | No |

DEPARTMENTS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
DEPARTMENTID| Integer | unique | Yes | No |
DEPARTMENT| VarChar(255)| string| No | No |

# Technologies Used

	### Tools

	- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
	- [MySQL](https://https://www.mysql.com/) is the database for this project locally.
    - [PostGres](https://www.postgresql.org/) is the database for this project when deployed on Heroku.
	- [GitHub](https://github.com/) to store and share all project code remotely. 
	- [Balsamiq](https://balsamiq.com/) used to create the wireframes for my project.

    ### Libraries

	- [JQuery](https://jquery.com) to simplify DOM manipulation.
	- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
	- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
	- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
	- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html.
	- [Google Fonts](https://fonts.google.com/) to style the website fonts.
    - [Stripe](https://stripe.com/docs) A python library to talk to Stripe's API for card transaction payments.
    - [psycopg2](https://www.psycopg.org/docs/) A database adaptor for PostgreSQL with Python.
    - [Django](https://www.djangoproject.com/) Python web framework used in order to build dynamic applications.

    	### Languages
	The project uses HTML,CSS, Javascript and python programming languages.
	- [HTML](https://en.wikipedia.org/wiki/HTML5) to construct and render pages.
	- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to simplify displaying data from the backend of this project smoothly and effectively in html.
	- [Javascript](https://www.javascript.com/) to style the website fonts.
    - [Python](https://www.python.org/) to style the website fonts.