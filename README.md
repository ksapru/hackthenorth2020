# Hack the North 2021 - IntAI

AI generated interview feedback to help you land your next job

[Check out the presentation](https://youtu.be/Lqp7wWTg9aU)

[Check out our demo](https://youtu.be/sjuOOy8BoxU)

[Check out our DevPost](https://devpost.com/software/intai)

## Inspiration
As students, it can be stressful and difficult preparing for interviews. Whether it’s your next job interview or applying to universities. Additionally, online interviews pose an even greater challenge as it adds an additional degree of separation between you and the interviewer. There currently exist many paid online services where you can book a time with a coach to do a mock interview. However, not everyone has the money or time for this. We hope to provide a quick, accessible, and convenient way for students and job seekers alike to prepare for their interviews and get feedback instantly.


## What it does
When the user goes to our web app, they can generate a practice interview question and record themselves as they answer the question, then the program analyzes the video by parsing the audio from speech to text and running image recognition. Then it provides the user with feedback on their speech and eye contact and facial expressions.
These practice interviews are meant mainly for behavioral-based interviews

## How we built it
The Frontend was made using React, while the backend is made using Flask. We used several google cloud APIs including storage, natural language processing, vision, text to speech, and video intelligence API to process the video and audio feed received from the front end. We used cockroachDB to host a large bank of practice interview questions.

## Challenges we ran into
- First, we ran into the challenges of setting up the google cloud and cockroachDB API's, learning how to use them, and how to integrate them into our code.
- Integrating frontend and backend posed to be a huge challenge for us
- One of our members is completely new to web development and had a steep learning curve for the frontend development

## Accomplishments that we’re proud of
- Learning how to integrate react and flask
- Learning to use different API's

## What we learned
- How to integrate react and flask together
- How to use cloud storage and other API’s by Google Cloud
- Using React
- How to use cockroachDB as a database

## What's next for IntAI
We hope to implement additional features such as real-time tips based on the current video feed. Such as suggestions to smile, make eye contact with the camera when the program notices that the user has not done so in a while. We also hope that our natural language processing can be extended further to highlight key points and phrases in sentences

We also hope to deploy it to our registered domain: prepforthatinterview.online