# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The scenario chosen for this task is a Student Academic Information Assistant.

The system contains private academic information about a student and the credit values of selected subjects.

The student information used in the scenario is:

- Student Name: Saruthi
- Department: CSE
- Semester: 5
- CGPA: 7.81

The subject credit information is:

| Subject | Credits |
|---|---:|
| CS501 | 4 |
| CS502 | 3 |
| CS503 | 4 |
| CS504 | 3 |

The system is tested using questions such as asking for the credits of a subject, calculating the total credits of two subjects, comparing the credits of two subjects, generating a study encouragement message, and finding two subjects that can be taken within a given credit limit.

---

# 2. Plain Chatbot

The plain chatbot uses an LLM to generate responses to the user's questions. It does not directly access the private student information or the subject-credit dictionary through a tool.

The chatbot sends the user's question to the LLM and receives the generated response. It does not have predefined Python rules for retrieving subject credits.

This approach is flexible because the LLM can respond to different types of questions, including questions that are not related to academic data. However, it can produce incorrect information when the answer depends on private data that has not been provided to the model.

For example, when asked about the credit value of CS501, the chatbot may not know the actual value stored in the private data and may generate an unsupported answer.

The main limitation of the plain chatbot in this scenario is that it has no direct mechanism to retrieve the private academic information.

---

# 3. Rule-Based Workflow

The rule-based workflow uses predefined Python rules and does not use an LLM.

The workflow accesses the subject-credit dictionary directly. It identifies subject codes such as CS501 and CS503 from the user's question and uses predefined conditions to determine the appropriate response.

For example, if the question asks for the credits of one subject, the workflow retrieves the corresponding value. If the question asks for the total credits of two subjects, it adds their credit values.

This approach provides predictable results for questions that match the predefined rules. However, it is less flexible when the user asks a question that was not anticipated while designing the rules.

In this scenario, the workflow can handle direct credit queries, total-credit calculations, and some comparison questions. It cannot naturally handle open-ended requests such as generating an encouragement message or finding subject combinations unless additional rules are specifically programmed.

---

# 4. AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent has access to two tools:

1. `get_subject_credits` — retrieves the credit value of a subject from the private subject-credit data.
2. `calculator` — performs arithmetic calculations.

When a user asks a question, the LLM first determines whether a tool is required. If a tool is required, the agent calls the appropriate Python function. The result is returned to the LLM, which can then decide whether another tool is needed. This process continues until the agent can produce a final answer.

For example, for a question asking for the total credits of CS501 and CS503, the agent can retrieve both credit values and then use the calculator to add them.

For a multi-step question such as finding two subjects within a credit limit, the agent can retrieve subject information, perform calculations, and use the results to form an answer.

The main limitation is that the agent depends on the LLM's decisions about which tools to use and how to solve the problem. Therefore, its behavior can be less predictable than a fixed workflow.

---

# 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for natural-language responses | Low because rules are predefined | High because the LLM can choose actions |
| Decision-making | LLM generates the response | Python conditions determine the response | LLM decides which tools and steps are needed |
| Tool usage | No tools | No LLM tools | Uses subject lookup and calculator tools |
| Private-data access | No direct access to the private dictionary | Direct access through Python | Accesses private data through tools |
| Multi-step task handling | Limited and may guess | Limited to predefined rules | Can perform multiple tool calls in a loop |
| Automation | Can generate responses automatically | Automates predefined cases | Can automate dynamic multi-step tasks |
| Reliability | Can generate unsupported information | Predictable for covered cases | Depends on correct tool selection and reasoning |

---

# 6. Suitability Analysis

For this student academic information scenario, the AI agent is suitable for questions that require multiple steps or dynamic use of the academic data.

The plain chatbot is useful when the user mainly needs general conversational responses that do not depend on private academic information.

The rule-based workflow is suitable for simple and predictable academic queries where the required rules are known in advance. For example, retrieving the credit value of a known subject can be handled using a fixed rule.

The AI agent is useful when the question requires combining information retrieval with calculations or several actions. It can select the required tools and continue working until it reaches a final answer.

Therefore, the appropriate approach depends on the type of question. Simple fixed questions can be handled using rules, general conversational questions can use a chatbot, and dynamic multi-step questions can use an AI agent.

---

# 7. Conclusion

This task demonstrated three different approaches to solving the same student academic information problem.

A plain chatbot mainly uses an LLM to generate responses. It is flexible but does not automatically have access to the private academic data used in this scenario.

A rule-based workflow follows predefined Python conditions. It provides predictable results for the cases covered by its rules, but its flexibility is limited when new types of questions are introduced.

An AI agent combines an LLM, tools, and a loop. The LLM decides which tools are required, the Python tools access the private data and perform calculations, and the loop allows the agent to continue taking actions until the task is completed.

In general, a chatbot is appropriate for conversational responses, a rule-based workflow is appropriate for predictable and well-defined processes, and an AI agent is appropriate when a task requires flexible decision-making, tool usage, and multiple steps.

---

# Day 2 Task: Reasoning and Acting — Direct Prompting, Chain-of-Thought, and ReAct

## 8. Scenario

For this task, a course-fee comparison scenario was selected.

The question is:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

The ReAct agent has access to two tools:

1. `get_course_fee(course_code)` — retrieves the fee of a course.
2. `calculator(expression)` — performs arithmetic calculations.

During the ReAct experiment, the agent retrieved the following fees:

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

The calculations were:

- CS101 + AI202 with 10% scholarship:
  `(12,000 + 18,000) × 0.90 = Rs. 27,000`

- All three courses with 25% scholarship:
  `(12,000 + 18,000 + 15,000) × 0.75 = Rs. 33,750`

- Difference:
  `33,750 - 27,000 = Rs. 6,750`

Therefore, the first option is cheaper by Rs. 6,750.

---

## 9. Direct Prompting

Direct prompting asks the LLM to provide an answer directly without using tools or showing step-by-step reasoning.

For this scenario, the direct-prompting program produced:

> Cannot determine without the course costs.

This result occurred because the model did not have access to the actual course-fee information through a tool.

Direct prompting is useful when the required information is already available in the prompt or within the model's available knowledge. It is simple and fast, but in this scenario it could not retrieve the missing course fees.

---

## 10. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to solve a problem step by step.

For this scenario, the model identified the required course prices, represented the scholarship calculations using formulas, and explained how the two options should be compared.

However, the actual numerical course fees were not provided to the model. The model therefore concluded that it could not determine the final numerical answer.

This demonstrates that Chain-of-Thought can help with multi-step reasoning, but it cannot obtain external information by itself when that information is missing.

---

## 11. ReAct Agent

The ReAct approach combines reasoning with actions and observations.

For the selected scenario, the agent used the following tool calls:

1. `get_course_fee("CS101")` → Rs. 12,000
2. `get_course_fee("AI202")` → Rs. 18,000
3. `get_course_fee("DS303")` → Rs. 15,000
4. `calculator("12000+18000")` → Rs. 30,000
5. `calculator("0.9*30000")` → Rs. 27,000

The agent then produced the complete comparison:

- First option = Rs. 27,000
- Second option = Rs. 33,750
- Difference = Rs. 6,750

The final answer was that CS101 and AI202 with a 10% scholarship were cheaper by Rs. 6,750.

The main advantage in this scenario is that ReAct can obtain information using tools before producing the final answer.

---

## 12. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Direct answer with no visible reasoning | Step-by-step reasoning | Reasoning combined with actions and observations |
| Tool usage | No tools | No tools in this experiment | Uses course lookup and calculator tools |
| Reliability on multi-step questions | Can be limited when information is missing | Better for multi-step reasoning when required information is available | Can handle multi-step problems involving external information |
| Transparency | No visible reasoning | Reasoning steps are requested and shown | Tool actions and observations are visible |
| Speed / cost | Generally fastest | Longer responses require more tokens | Additional tool calls increase processing |
| Consistency across repeated runs | Can vary depending on temperature and model | Can vary across reasoning paths | Depends on the model, tool calls, and execution |

---

## 13. Self-Consistency Observation

The self-consistency experiment used the following reasoning question:

> A student takes three courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment?

The correct answer is Rs. 9,562.50.

At temperature 0.8, all five runs produced the same numerical answer, Rs. 9,562.50, but the wording was different between runs.

The program compared the complete extracted answer strings, so it reported a majority of 1 of 5 even though all five responses contained the same numerical answer.

The temperature was then changed to 0.

At temperature 0, all five runs produced Rs. 9,562.50 with effectively identical wording. The program therefore reported:

> Majority answer (5 of 5 runs)

The experiment showed that non-zero temperature can produce variation in responses, while temperature 0 produced consistent responses for this question and model.

---

## 14. Suitability Analysis

For the selected course-fee scenario, ReAct is suitable because the problem requires external information as well as reasoning.

Direct prompting could not determine the answer because the course fees were not available to the model. Chain-of-Thought could reason about the required formulas but also could not retrieve the missing course fees.

The ReAct agent was able to retrieve the course fees through tools and then use the obtained information to calculate the final comparison.

Therefore, this scenario demonstrates why tool access can be important when a question requires information that is not already available to the model.

Self-consistency was useful for examining repeated reasoning responses, but it did not provide missing external information. The model still required the relevant facts before it could perform the calculation.

---

## 15. Conclusion

The three approaches handle problems differently.

Direct prompting is appropriate for straightforward questions where the required information is already available and a direct response is sufficient.

Chain-of-Thought is useful for multi-step reasoning and calculation problems when the required information is already available to the model. It allows the model to work through the problem step by step.

ReAct is appropriate when a problem requires both reasoning and external information or actions. It can determine what information is needed, call a tool, observe the result, and continue until it can produce a final answer.

The course-fee scenario demonstrated this difference. Direct prompting could not obtain the missing course fees. Chain-of-Thought could explain the calculation process but could not retrieve the missing values. ReAct used tools to obtain the course fees and reached the correct answer of Rs. 6,750 difference.

Thus, the appropriate approach depends on the problem: direct prompting for straightforward questions, Chain-of-Thought for multi-step reasoning with available information, and ReAct when reasoning needs to be combined with external tools or actions.