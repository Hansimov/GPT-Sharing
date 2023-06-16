---
markmap:
  colorFreezeLevel: 4
  duration: 250
---


# <root>Prompts Cheat Sheet<br><ft>(Group by Principles)</ft></root>

## <l2>More Informative</l2>
### <l3>Detailed ...</l3>
- Roles
  - <pr>Act as Python expert</pr>
  - <pr>You are an experienced Frontend programmer</pr>
- Scenarios, Contexts
  - <pr>I’m writing a Python Project</pr>
  - <pr>You are developing a concurrent program for data processing</pr>
- Instructions
  - <pr>You should extract all definitions of functions from this script</pr>
  - <pr>You task is to complete this script with a timeit feature</pr>
  - <pr>I would like to add an web UI to this</pr>
- Questions
  - <pr>Could you give some suggestions on this plan</pr>
  - <pr>Can you summarize the goal of the codes</pr>
### <l3>Additional ...</l3>
- Examples, Shots
  - <pr>Here is an example</pr>
  - <pr>The output should be similar to the following formats</pr>
  - <pr>You should use same method in the provided script</pr>
- Choices, Options, Paths
  - <pr>You could use \`requests\` library to do http GET and POST operations</pr>
  - <pr>You can try different backend frameworks such as Django or Flask or FastAPI</pr>

## <l2>Less Ambiguous</l2>
### <l3>Formatted ...</l3>
- Inputs
  - <pr>I would provide you a JSON file which contains the data of ...</pr>
  - <pr>The contents in triple backticks are the Python codes for ... that I want to improve: <br>\`\`\`py<br>(Here are the codes)<br>\`\`\`</pr>
- Outputs
  - <pr>Answer in table format</pr>
  - <pr>List the outline with numbered bullets at beginning of line</pr>
  - <pr>You should only output the changed lines in git diff format:<br>\`\`\`diff<br>-- original lines<br>++ modified lines<br>\`\`\`</pr>
### <l3>Limited ...</l3>
  - Length
    - <pr>Your answer should be no more than 50 words</pr>
  - Content
    - <pr>Do not output whole script, but only output changed functions</pr>
  - Style
    - <pr>Your response style should be academic and professional</pr>
  - Tools
    - <pr>You should only use Python standard library</pr>
### <l3>Prioritize/Emphasize/Focus/Repeat <br> <ft>(Do ONE thing and do it WELL)</ft></l3>
  - <pr>Let's focus on the code implementations of this function</pr>
  - <pr>Let's go back to the topic / task of ...</pr>
  - <pr>Let's dive deeper and move forward in the step of ...</pr>


## <l2>Keep Iterating</l2>

### <l3>Chain/Tree of Thoughts<br><ft>(Many a little makes a mickle)</ft></l3>
- Break to Subtasks / Steps
  - <pr>Here is a math question: ... Let's think step by step</pr>
  - <pr>I would like to ..., you should:<br>1st ... 2nd ... 3rd ...</pr>
  - <pr>Please do the following steps:<br>[1] ... [2] ... [3] ... [4] ...</pr>

- Search before Reason,<br>Plan before Action
  - <pr>Search the web first, then examine the results, then plan the steps to ...</pr>
  - <pr>Analyze the requirements first, then re-organize them into a list of tasks,<br>then do the tasks one by one</pr>

- Create Multiple Paths
  - <pr>For this task, you should provide three solutions</pr>
  - <pr>Analyze this problem from following perspectives respectively:<br>[1] Product Managers; [2] Software engineers; [3] Users.</pr>

- Combine to Summary / Best Solution
  - <pr>Review the steps above, and suggest a better solution</pr>
  - <pr>Recall all our conversations, and summarize the key points</pr>
  - <pr>Evaluate results of the solutions above, recommend the best one</pr>



### <l3>Automation</l3>

- Self Ask/Search
  - <pr>Search you knowledge base, and list ...</pr>
  - <pr>Suggest three instructions which I might ask you to do for diving deeper and moving forward in this task</pr>
- Self Check/Criticize
  - <pr>Please Rephrase/Check/Feedback/Refine/Criticize your answer above</pr>
  - <pr>Design several indicators to evaluate the solutions you suggest above</pr>
  - <pr>Recommend the best solution based on reasonable aspects</pr>