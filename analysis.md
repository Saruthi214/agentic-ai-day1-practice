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