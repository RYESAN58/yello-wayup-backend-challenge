# URL Shortener

## Objective 
Your assignment is to implement a URL shortening service.

## Brief
ShortLink is a URL shortening service where you enter a URL such as https://yello.co/directory1/directory2/resource and it returns a short URL such as https://short.est/GeAi9K.

## Tasks 
- Implement the assignment using: 
  - Language: Python
  - Framework: Your choice, Django, Flask or any other you prefer. Framework is optional, not required.
- Two endpoints are required:
  1. /encode - Encodes a URL to a shortened URL
  2. /decode - Decodes a shortened URL to its original URL. 
- Both endpoints should return a JSON response.
- There is no restriction on how your encode/decode algorithm should work. You need to ensure that a URL can be encoded to a short URL and the short URL can be decoded to the original URL. You can persist the short URLs and Long URLs in a database, but it's optional.
### Optional Tasks:
- Add authentication and authorization to ensure that only authenticated users can use the service to encode URLs.

## Evaluation Criteria
* Coding Language best practices
* API implemented featuring an `/encode` and `/decode` endpoint
* Show us your work through your commit history
* Completeness: Did you complete the features? Are you able to demonstrate that?
* Correctness: Does the functionality act in sensible, thought-out ways?
* Maintainability: Is it written in a clean, maintainable way?
* Use of AI: You are expected to be able to showcase, explain and iterate over your code. AI usage is allowed as a programming aide, but **do not simply copy/paste AI-generated code**.

**It doesn’t have to be perfect. Writing code always involves trade-offs and design decisions. The most important thing is your ability to speak about the decisions you have made.**

## Submission Process:
* Please submit your code in a new GitHub repository. You can start by forking this repository into your account and then create a clone of it locally.
