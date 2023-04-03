# stba-facial-recognition
Encoding Faces Within Images

Facial recognition is a modern and widely used authentication technique in mobile technologies. The software engineering team at SBA is constantly working to improve this technology. As a junior software engineer, it is your job to work on enhancing this feature.

The overall objective for this task is simple. Write some code that transforms an image (of a person's face) into a vector and deploy this as an AWS Lambda function.

The MLE team will then train their machine learning models using the resulting vectors. It is important to note that the quality of these vectors is critical for the MLE team. The security lead has sent you the following email with further details about this task:

Good afternoon,

Well done with the JWT task! Now we’d like you to focus on the facial recognition authentication system.

This task is for you to build a Python Lambda function for deployment on AWS. The function must read a single image file from AWS S3 and output a vector.

The process of transforming a file into a numeric vector format is called encoding. How you encode the image file is very important because we want to include as much helpful information from the image file as possible within the encoded representation.

The encoding method is important because the machine learning engineering team will use these vectors to train models. Therefore, the more each vector properly represents the features within their respective images, the better the data quality used to train the models.

When building the Lambda function, you should follow these guidelines:

Assume that the Lambda function will be run once per image, so only one image will be read from S3 to the function at a time.
Each image file should be encoded into a vector of the same length each time.
The software engineering team will review this code. To demonstrate how the Lambda function will read data from S3, include the relevant packages and code and include comments to explain what the code should be doing.
You will not be given any AWS credentials at this point, so as long as the structure of your Lambda code is good, this will suffice. We don’t expect you to create resources on AWS to test the Lambda code running.
Please include a file named “requirements.txt” that includes any required packages that require installation to run your Lambda function.
When finished with development, please send me all your files compressed into a folder for the team to conduct a code review.

Best regards

To complete this task, you will need to research ways to encode facial image features into a descriptive vector and test the implementation locally using the sample dataset before writing the Lambda function.


