<div align="center">
<img src="https://github.com/tdignan87/traceVMS/blob/master/static/img/TraceSense_RGB.jpg" target="_blank" rel=""/>
</div>
<div align="center">
<h1>TraceSense - Traceability Company</h1>
</div>

## Introduction

Tracesense is an application used for conducting GMP(good manufacturing practice) audits electronically. Tracesense will allow the user to complete the audit via a tablet, phone, or PC and there is no installation required.<br> Tracesense also allows for completing glass and hard plastic audits which is a food safety requirement.

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
specifically designed so they can complete audits easily without having to record it on paper and then update an excel document at a later stage.

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

* Google Font [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro) was chosen as it looks great across multiple interfaces.

### Colours

* The colours for this project were choosen based on the two primary colours in my company logo. These colours are

- ![#0069A8](https://via.placeholder.com/15/0069A8/000000?text=+) `#0069A8`
- ![#42BFE0](https://via.placeholder.com/15/42BFE0/000000?text=+) `#42BFE0`

## Wireframes

The wireframes were created using [Balsamiq](https://balsamiq.com/) during the scope part of the design and planning process for this project. I found Balsamiq very useful for helping me plan out exactly what i needed for my application to come together.

To go to the main wireframes page please click [this](https://github.com/tdignan87/TraceSense/tree/master/wireframes) link.

#### Browser

- [Browser Main Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-main-page.png)
- [Browser Register Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-sign-up.png)
- [Browser Signed In Page](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-sign-in-home.png)
- [Browser Sign Up](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-sign-in-home.png)
- [Browser Start Audit](https://github.com/tdignan87/TraceSense/blob/master/wireframes/browser-start-gmp-audit.png)
- [Browser Completed Tasks](https://github.com/tdignan87/TraceSense/blob/master/wireframes/completed-tasks.png)
- [Browser Outstanding Tasks](https://github.com/tdignan87/TraceSense/blob/master/wireframes/outstanding-tasks.png)
- [Browser Recipient List](https://github.com/tdignan87/TraceSense/blob/master/wireframes/recipient-list.png)




## Flow Chart

Still to be completed this section.

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


# Information Architecture

[MySQL](https://www.mysql.com/) was the database choice for my project. An relational database management system was the most appropriate database choice for this project. 


Typical types of data stored in the database are

- Id
- Int
- String
- Boolean
- DateTime

Tracesense relies on the following data structure:

TBL_GMP_QUESTIONS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
GMP_QUESTIONID | Integer | unique | Yes| No |
QUESTION | VarCar(255) | text | No| No |
CREATED | DateTime | DateTime | No| No |
DELETED | bool | bool | No | Yes |


TBL_GHP_QUESTIONS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
GHP_QUESTIONID | Integer | unique | Yes | No |
QUESTION | VarChar(255) | text | No | No |
CREATED | DateTime | DateTime | No | No |
DELETED | bool | bool | int | Yes |

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

TBL_GHP_ANSWERS

| Title | data type | value | Primary Key | Allow Null |
--- | --- | --- | --- | ---
GHP_ID | Integer | unique | Yes | No |
GHP_QUESTIONID | int | unique | No | No |
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


