---
markmap:
  colorFreezeLevel: 4
  duration: 250
  extraCss:
    - "./prompts-cheat-sheet.css"
---


# <root>Prompts Engineering Cheat Sheet</root>

## <l2>More Informative</l2>
### <l3>Detailed ...</l3>
- Roles
  - Act as Python expert
  - You are an experienced Frontend programmer
- Scenarios, Contexts
  - I’m writing a Python Project
  - You are developing a concurrent program for data processing
- Instructions
  - You should extract all definitions of functions from this script
  - You task is to complete this script with a timeit feature,
  - I would like to add an web UI to this
- Questions
  - Could you give some suggestions on this plan
  - Can you summarize the goal of the codes
### <l3>Additional ...</l3>
- Examples, Shots
  - Here is an example
  - The output should be similar to the following formats
  - You should use same method in the provided script
- Choices, Options, Paths
  - You could use \`requests\` library to do http GET and POST operations
  - You can try different backend frameworks such as Django or Flask or FastAPI

## <l2>Less Ambiguous</l2>
### Formatted ...
- Inputs
  - The contents in triple backticks are the Python codes for ... that I want to improve: <br>\`\`\`py<br>(Here are the codes)<br>\`\`\`
  - I would provide you a JSON file which contains the data of ... : <br>\`\`\`json<br>(Here is the JSON data)<br>\`\`\`
- Outputs
  - Answer in table format
  - List the outline with numbered bullets at beginning of line
  - You should only output the changed lines in git diff format
### Limit / Constraint ...
  - Length, Size
    - Your answer should be no more than 50 words
  - Content
    - Do not output whole script, but only output changed functions
  - Tools
    - You should only use Python standard library
### Prioritize/Emphasize/Focus/Repeat <br> <small>(Do ONE thing and do it WELL)</small>
  - Let's focus on the code implementations of this function
  - Let's go back to the topic / task of ...
  - Let's dive deeper and move forward in the step of ...

## <l2>Top-Down</l2>
### Divide and Conquer (Sub-tasks)
### Recursion
### Search then Reason, Plan then Action
  - Search the web first, then examine the results, then plan the steps to ...
  - Analyze the requirements first, then re-organize them into a list of tasks, then do the tasks one by one

## <l2>Bottom-up</l2>
### Dynamic Programming
### Memorization
### Quantitative to Qualitative <br> <small>(Many a little make a mickle)</small>

## <l2>Iterate</l2>

### Self Ask / Search
- Search you knowledge base, and list ...
- Suggest three instructions which I might ask you to do for diving deeper and moving forward in this task
### Self Check / Criticize
- Please Rephrase/Check/Feedback/Refine/Criticize your answer above
- Design several indicators to evaluate the solutions you suggest above
- Recommend the best solution based on reasonable aspects

### Chain of Thoughts/Actions <br> <small>(Think/Act Step-by-step)</small>
- Let's think step by step
- Please answer these questions one by one
- I would like to ..., you should:<br>1st ... 2nd ... 3rd ...
- Please do the following steps:<br>[1] ... [2] ... [3] ... [4] ...

## <l2>Hacker Spirit</l2>
### Inject
### Leak
### Jailbreak
