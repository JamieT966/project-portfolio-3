# Chemstore Group Chemical Safety Quiz

![Chemstore Logo](media/chemstore_logo.png)

[Chemstore Chemical Awareness Quiz Live Site](https://jamiet966.github.io/project-portfolio-2/)

Chemstore Group conducts chemical awareness training throughout Ireland throughout the year, this quiz has been designed to aid in that training. This will allow the business to ensure clients are taking the information on board. This quiz will also add a fun, interactive element for their clients that will liven up their training days.

![Am I Responsive Image of Chemstore Quiz](media/responsive.png)

**The business goals of this quiz:**
* Adds something different to their training days.
* Break up the monotony of training days that can last several hours. 
* Ensure that clients are paying attention by testing their knowledge.

**The customer goals of this quiz:**
* Clear, easy and intuitive to use the quiz.
* Provide a fun and interactive quiz to users.
* To achieve a passing score.

## **Features**

### Start Page 

* Start page features the Chemstore logo, a title, an image of chemical CPL symbols, links at the bottom to access the company's website, LinkedIn and Twitter. As well as a start button that initiates the quiz and a rules button that pops out a modal with rules and instructions.

![Chemstore Quiz Start Menu](media/start.png)

### Rules Modal

* This modal displays the instructions and rules for the quiz.

![Chemstore Quiz Rules Modal](media/rules.png)

### Quiz Screen

* The quiz screen displays the same logo and links at the bottom as all other pages on this quiz.

* There is a question section, an answer choice section containing four buttons with a choice in each. 

* The quiz screen also features a next and restart quiz button.

![Quiz Screen](media/qscreen.png)

### Correct

* When a correct answer is selected the choice button that was selected will turn green with a message in the question zone displaying green correct text.

![Chemstore Quiz Correct Answer](media/correct.png)

### Incorrect

* When an incorrect answer is selected the choice button that was selected will turn red with a message in the question zone displaying red incorrect text.

![Chemstore Quiz Incorrect Answer](media/incorrect.png)

### Result Page

* The result page shows when the quiz has finished and displays your score.

![Chemstore Quiz Result Page](media/result.png)

### Features Left to Implement in The Future

* In the future, I would like to add a certificate that is automatically generated based on the user inputs, such as name, score, etc.

* I would also like to add more questions when I sit down with Chemstore to flesh out more content.

* There is a possibility of removing the restart button in the future as this becomes less of a quiz and more of a test. This would only show if the user receives a failing grade.

## **Testing**

### Validator Testing

* [W3C Markup Validation](https://validator.w3.org/)
* [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

I validated my HTML and CSS with the W3C Markup Validator and W3C CSS Validator to check the validity of my code.

### Client Story Testing

* I have added a rules modal at the start page to make the user aware of what is expected of them.

* There is currently a restart quiz button on every page so the user can restart the quiz at any time. The logo will also take the user back to the start screen as I believe that is expected of a logo.

* I have added a question counter to the top of the quiz screen. This makes it abundantly clear to the user exactly what question they are on and how many questions are left.

### Manual Testing

* I have tested all links and all internal and external links are fully working. I have also tested when clicking the site logo and that returns the user to the home page. Any external links have a ```target="_blank"```, ensuring they open in a new tab.

* The quiz only allows you to select one answer per question, it then disables all other choice buttons and displays a correct or incorrect message.

* The website has been tested across all major browsers (Chrome, Firefox, Edge, Safari, etc) and all emulated mobile devices using Google Chrome Developer Tools. While testing I realised that my website was not fully responsive on very small screens, such as an iPhone 5. I had to add width and max-width to resolve this.

* I ran a Google lighthouse report that had very good results. The full report can be read [here.](https://pdfhost.io/edit?doc=6fdd79c5-8798-4ea9-97fd-3e80b8b8397c)
![Google Lightouse Report](media/lighthouse.png) 

## **Bugs**

* A bug that I found while creating this quiz was that when transferring the score variable from one javascript file to another was that when all answers were correct it would be one scoreless. E.g. all answers are correct but 9/10.
I found that I was storing the score variable after I was directing the user to another page, meaning the score was 10 before clicking the next button but 9 after clicking the button.

* A second bug that myself and a tutor found was that any event listeners added into my javascript file outside a function threw an error. I resolved this by using onclick attributes in my HTML files.

## **User Experience**

### Strategy

The client wanted a quiz to aid in their chemical safety training. Chemstore travels out to host the event and would like a multiple choice quiz to test attendees knowledge either at the end of the day or halfway through the day.

### Scope

I discussed with the client and we decided the scope of this project together. I gave an overview of what was on the table. For example, the basic outline of the quiz was to be delivered with a variable keeping track of the current page and another variable keeping track of the user's score.

Unfortunately, due to time constraints, the ability to issue the user with a certificate based on score fell out of the scope for this project. This can be revisited at a later date.

### Structure

For the main structure, I implemented a start screen hosting a modal with the rules. Once the start button is clicked then the quiz begins. For continuity, the Chemstore logo stays fixed to the top and three links are fixed to the bottom. These link to the company's website, LinkedIn and Twitter.

All buttons colours invert when hovered over to demonstrate good interactive design.

A results page tells the user their score and whether or not they need to restart the quiz.

### Skeleton

Initially, I drew out all the functions required and a rough idea of how I wanted the quiz to look.

I then created a wireframe using Balsamiq. 

![Quiz Balsamiq Wireframe](media/wireframe.png)

### Surface

For colours, I went with the Chemstore brand colour palette as I felt these looked nice and it offered continuity across the Chemstore brand.

```--cgreen: #98c244; --cred: #e6554d; --cnavy: #2d3347; white #ffffff```

![Colour Pallete Used For Chemstore Quiz](media/colours.png)

## **Technologies**

1. HTML
2. CSS
3. JavaScript
4. Gitpod.io - for writing the code. Using the command line for committing and pushing to Git Hub
5. GitHub - Used to host repository
6. GIT - for version control of the project.
7. [Beautifier](https://beautifier.io/) - Used to beautify my HTML, CSS and JavaScript.

## **Deployment**

The website is hosted by GitHub Pages and the live page can be found here: [Chemstore Chemical Awareness Quiz](https://jamiet966.github.io/project-portfolio-2/)

**The Steps I Took To Deploy on GitHub Pages:**

1. Went to github.com
2. Under Repositories click on the desired project.
3. Click on Settings just over the green Gitpod button.
4. On the left navigation menu, find and click Pages.
5. Under Source, change Branch to main and the files to /root and click save.
6. Wait a few minutes and your repository will be live on Github Pages.

![Your Repository was Published](media/published.png)

As this website is hosted by GitHub pages it is directly deployed from the repository's master branch. This means that the deployed site will automatically update from any commits from the master branch of my repository.

**The Steps I Took To Push Changes to Live website:**

1. When have completed a section of code, in the terminal window: `git add .` or `git add index.html "or other file"`.
2. `git commit -m "Your commit message here`.
3. `git push`.

To run a local copy, you can clone into any editor by pasting this: `git clone https://github.com/JamieT966/project-portfolio-2.git` into your editor.

## **Credits**

### Content

* All content came from the Chemstore chemical awareness training PowerPoint presentation. This gave me everything I needed to create questions and answers.

### Media

* The Chemstore logo came from the Chemstore website. [Chemstore.ie](https://www.chemstore.ie/)

### Acknowledgments

* First and foremost my mentor Brian Macharia, has been a great help on this project.

* The Code Institute tutors, in particular, Rebecca and John were immensely helpful and patient guiding me through solving the issues I was having.

* I would like to credit this students quiz for giving me the idea of having a 'hide' class that could be toggled on and off depending on the need. [Geo Quiz](https://github.com/lee-joanne/geo-quiz)

* I also need to credit W3 schools for their modal instructions that I completely copied and then adjusted to the needs of my quiz. [W3 Schools Modals](https://www.w3schools.com/howto/howto_css_modals.asp)

* I also watched many YouTube videos for ideas but I did not follow any particular video.