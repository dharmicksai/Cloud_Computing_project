# A Scalable Design Approach for State Propagation in Serverless Workflow

This project contains an implementation of the design proposed in the paper 'A Scalable Design Approach for State Propagation in Serverless Workflow'. The implementation is done using python.
 
The design uses object serialization/deserialization with cloud object storage to share state across functions. It provides a mechanism for fine-grained support for state propagation and
synchronization in a serverless workflow. This solution is cost effective and efficient as it does not depend on any external database or cache for state management. The design has been validated by implementing ‘Word Count’- a classic MapReduce use case. 

In comparison to other popular programming languages, Python offers the most flexible serialization and deserialization of objects. Hence, python has been used for the implementation of the mapReduce algorithm for getting the word count of an input file. The Pickle module is used for serialization and deserialization.

## Team members:
 - Nanda Kishore - 191CS140
 - K Dharmick Sai - 191CS221
 - Aryaman M - 191CS211
