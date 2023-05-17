

## Test and Deploy


# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
TrenHard

## Description

I will be creating a fullstack web application that is a platform for people interested in their health that will allow people to signup and create a workout program for themselves or a suggested one, provide a meal program, and show nearest gyms by their location by inputting their address.
We will be using the Google Maps API, the myfitnesspal API,and exersiseDB API which are all free.

Finished working on Accounts Microservice after a few month hiatus. I was able to complete the views.py and debug the problems while maintaining RESTful practices as well as making sure that JWT authentication was possible. I checked and verified on Insomnia, the only one I did not test however was the delete but maybe I will try it later when it's not so late. Just tried it right now DELETE works and I was able to fix a POST bug for creating new accounts as it was spelled PUT instead of POST.
02/09/23 1:31 AM

Started working on the Workouts Microservice. Completed the models.py and debugged the views.py.I was having a bug where the container wasn't working do to this error,
"File "/usr/lib/python3.8/os.py", line 673, in __getitem__
  raise KeyError(key) from None"
It turns out the error was caused due to the workouts.urls.py having an unnecessary path('', include('djwto.urls')) in it as it would look for a signin key that did not even exist. For the time being I will continue working on debugging and getting the rest of the model to work and incorporate CRUD for exercises and workouts next.
04/25/23 8:55 PM

I fixed the issue with the Workouts Microservice, and I have come to the conclusion that I will no longer use a Workouts API in the backend. Instead I will either incorporate the workouts myself with CRUD commands or I pull it onto the front end aspect of the server where I will use an API. However, I will still need to have the workouts communicate with the accounts API.
05/17/23 2:21 PM


## Goal
The main goal of this project is for me to learn and challenge myself into making a Full-stack Web application using Django and React on my own this time.


## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
