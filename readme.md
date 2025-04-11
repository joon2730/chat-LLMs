# ChatLLMs
Chat with LLMs as if they are your best friends!

## Project Goal
ChatLLMs aims to create a chat agent that engages in natural human interactions, delivering fun and immersive conversations that are indistinguishable from those with a real person.

## ToDo
- Implement **memory management**
    - [ ] Remember past chat history
    - [ ] Forget old/tivial memories for optimization
    - [ ] Learn about the user accumulatively from conversations
- Implement **natrual flow** in conversations
    - [ ] Aware of real-time information such as time, weather, news, etc
    - [ ] Can take initiatives in conversation (not the robotic QnA pattern)
    - [ ] Chat asynchronously using event and buffer (asynchronous workflow like humans)
- Implement **personalities** in LLMs
    - [ ] Preset personality type with options, or
    - [ ] Personality evolving over time depends on conversations
    - [ ] Have emotions and whims (randomness)


## Dev Notes
### Currently..
- Have a short-term memory (can't save and load memory)
- Random persona when initialized

### Next step
- Implement ascynchronous workflow of chatbot and interface(streamlit)
- Give chatbot a tool to access to real-time data
- Use langgraph to improve workflow