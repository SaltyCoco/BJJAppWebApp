# BJJAppWebApp


This is a web application built using plotly's Dash library.
Dash is built on top of Flask and retains all of Flask's
capabilities.  

This app would be deployed via aws elastic beanstalk or ECS
depending on whether I wanted to containerize it.  The app
is connected to a DynamoDB backend and would have all the 
access keys stored in aws secret manager.

Authentication would be done using react.js as it 
is integrated with cognito and, especially, amplify.

I really like using Dash and aws to deploy analytics sites.
Dash solely does not provide everything that could possibly be
needed with an enterprise system but from within a properly
maintained aws infastructure it could..
