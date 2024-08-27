# Assignment: Advanced Design Patterns in Practice

## Overview
In this assignment, you will explore and apply key design patterns to a practical scenario. The goal is to deepen your understanding of both the theory and application of design patterns in real-world software development. You will be required to study the provided materials on design patterns, implement specific patterns in a given scenario, test your implementations, and reflect on alternative approaches.

## Unit 3: Design Patterns I
- Introduction to Design Patterns
- Creational Patterns: Singleton, Factory, Builder
- Structural Patterns: Adapter, Composite, Proxy
- Behavioral Patterns: Strategy, Observer, Command

## Scenario: Smart Home Automation System
You are tasked with designing a Smart Home Automation System that manages various devices like lights, thermostats, security cameras, and door locks. The system should be scalable, maintainable, and flexible enough to accommodate new types of devices and user commands in the future.

## Tasks

### 1. Theory Deep Dive (20 points)
Before starting the practical tasks, you must research the following design patterns:

- **Creational Patterns**: Singleton, Factory, Builder
- **Structural Patterns**: Adapter, Composite, Proxy
- **Behavioral Patterns**: Strategy, Observer, Command

For each pattern, provide a brief explanation that includes:
- **Intent**: What problem does the pattern solve?
- **Structure**: A simple class diagram or description of how the pattern is structured.
- **Applicability**: Scenarios where this pattern is appropriate.
- **Pros and Cons**: Advantages and potential drawbacks of using the pattern.

Submit your explanations in a Google Doc with edit access to `chikwajacobos@gmail.com`.

### 2. Pattern Implementation (50 points)
Using the Smart Home Automation System scenario, implement the following patterns:

- **Singleton**: Ensure that only one instance of the `SmartHomeController` exists throughout the system.
- **Factory**: Create a `DeviceFactory` to manage the creation of different device types (e.g., Lights, Thermostats).
- **Adapter**: Implement an `Adapter` to integrate third-party smart devices that do not follow the standard interface of your system.
- **Strategy**: Allow users to configure different strategies for automating their home, such as "Energy Saving Mode" or "Security Mode."
- **Observer**: Notify users when specific events occur (e.g., security breach detected, temperature drops below a threshold).
- **Proxy**: Secure access to sensitive devices (like door locks) using a `Proxy` that controls access based on user permissions.

### 3. Testing and Validation (20 points)
For each pattern you implement:
- Write unit tests to validate that the pattern works as expected.
- Explain how you tested the pattern, what you expected to happen, and what actually happened.

Document your testing process in the README file of your GitHub repository.

### 4. Reflection and Alternatives (10 points)
Reflect on the design patterns you implemented:
- Were there alternative patterns you could have used? Why did you choose the ones you did?
- Discuss any challenges you faced while implementing the patterns.
- If you were to scale this system for a larger environment (e.g., managing hundreds of devices across multiple buildings), how might your design need to change?

## Submission Instructions
1. **Google Docs**: Submit a link to your Google Doc containing the theory explanations. Ensure that you have given edit access to `chikwajacobos@gmail.com`.
2. **GitHub Repository**: Create a GitHub repository for your code. Include:
   - The full implementation of your Smart Home Automation System with the patterns integrated.
   - A README.md file explaining how to run the system, your testing process, and your reflection.
   - Submit the link to your repository along with your Google Docs link.

## Deadline
Please submit your assignment by **[Insert Deadline Date Here]**.

## Additional Resources
To help you complete this assignment, consider reviewing the following resources:
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) by Erich Gamma et al.
- [Refactoring: Improving the Design of Existing Code](https://refactoring.com) by Martin Fowler
- [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/) by Eric Freeman and Elisabeth Robson

## Important Notes
- Ensure your code is clean, well-documented, and adheres to best practices.
- While collaboration is encouraged, ensure that the work you submit is your own. Plagiarism will not be tolerated.
- Pay attention to the theoretical part of this assignment; understanding the "why" behind design patterns is as important as knowing how to implement them.
