# Lecture 03 - Distributed Transport and Streaming

This week's exercises will use the case-based structure described in the general overview from Lecture 01's exercise. To summarize the process:

- You will be presented with a case that needs solving.
- You must design the architecture you believe can solve this problem (use your preferred drawing tool, e.g., draw.io, Excalidraw, etc.).
  - Ideally, using the technologies covered in the course so far.
  - You will receive feedback on your proposed architecture from the instructors.
- Once the architecture has been drawn, try to assemble it using the selected technologies and blueprints.

The process can be visualized as follows:

```mermaid
flowchart LR
    start@{ shape: circle, label: "Start" }
    case@{ shape: doc, label: "Read the case" }
    arch@{ shape: docs, label: "Draw your proposed architecture for the case" }
    feedback@{ shape: note, label: "Get feedback on your architecture from the instructors" }
    impl@{ shape: processes, label: "Implement architecture in Kubernetes" }
    test@{ shape: process, label: "Test architecture" }

    stop@{ shape: dbl-circ, label: "Done" }


    start-->case-->arch-->impl-->test
    arch-->feedback-->arch

    test-->|"If not compliant with the requirements"|arch
    test-->|"If compliant with the requirements"|stop
```

## New Technologies

The new technologies introduced this week are: **Kafka, Kafka Connect, KSQLDB, Flume, and Sqoop**.

For some general quick start guidance on utilising the technologies, please view the archived exerises from [Lecture 03 E24](https://github.com/JakobHviidBDDST/BigDataCourseExercises/tree/main/archive/E24/03).

## Case Description

PowerGrid Analytics LLC monitors an electric power grid, where they measure the wattage used. They obtain their data from multiple sources with different sample rates, each identified by a unique ID. They need to collect and store this data immediately.

However, they already have large amounts of telemetry on the grid stored in a SQL-based database that needs to be integrated into a new system with continuous data streams.

There are also rumors that some former employees have mountains of unorganized data stored outside their databases, which they claim is essential to the operation of the grid...👷🏽‍♂️


### Solution Requirements

- The solution must ingest large amounts of data from multiple sources in real time.
- The solution should be capable of ingesting structured database information. 
- The solution should be capable of processing unstructured data. 
- Streams should be routed and processed by sensor ID.
- The solution must persist the data to a distributed filesystem.

### Demonstrate

- How to do live ingestion of data from multiple sources.
- How to ingest structured data from a database.
- How to transfer data from a stream processing platform to long-term distributed storage.
- How to process and route streaming data in real-time.

### Remember to

- Identify bottlenecks.
- Pick appropriate ingestion technologies.
- Consider how scalability will be handled.
- Address data flow.
- Present arguments for:
  - The chosen streaming architecture format.
  - The chosen integration tools.
  - The chosen technologies.
