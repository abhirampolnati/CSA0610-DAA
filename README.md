# ShopSphere – Scalability Audit of an E-Commerce Platform

## 1. Project Overview

The ShopSphere Scalability Audit is a Design and Analysis of Algorithms (DAA) project that evaluates the efficiency and scalability of algorithms used in an online shopping platform. The project examines how different algorithms behave as the product catalogue grows from 100,000 products to 1,000,000 products.

The audit focuses on algorithmic time complexity, space complexity, recurrence relations, asymptotic notations, and execution-time estimation. The results are used to identify performance bottlenecks and recommend suitable algorithmic improvements.

## 2. Problem Statement

ShopSphere is an expanding e-commerce platform that performs several backend operations, including duplicate-product detection, API request auditing, product searching, product recommendations, and sales analytics.

As the number of products increases, the existing algorithms may require significantly more processing time and computational resources.

The objective of this project is to analyze five backend modules, determine their algorithmic efficiency, estimate their execution times, and recommend redesigns for algorithms that cannot meet the platform's nightly processing requirements.

## 3. Project Objectives

* Analyze the basic operations performed by each backend module.
* Determine time and space complexities using asymptotic notations.
* Derive exact operation counts for iterative algorithms.
* Solve recurrence relations using backward substitution and the Master Theorem.
* Analyze best-case, average-case, and worst-case performance.
* Prove asymptotic bounds using formal mathematical definitions.
* Estimate execution times for a catalogue containing 1,000,000 products.
* Identify performance bottlenecks and recommend scalable algorithmic solutions.

## 4. Modules Under Analysis

### M1 – Duplicate-Listing Detector

Examines product pairs to identify duplicate listings from the same seller.

### M2 – API Rate Limiter

Audits API requests over windows whose sizes double during each iteration.

### M3 – Product Search

Compares sequential searching with binary searching on a sorted product index.

### M4 – Recommendation Engine

Evaluates the existing recommendation algorithm and a proposed redesign that removes replicated processing.

### M5 – Sales Analytics Engine

Analyzes the recursive processing of sales records and determines the algorithm's asymptotic complexity.

## 5. Analysis Techniques

The project applies the following Design and Analysis of Algorithms concepts:

* Basic operation counting
* Time and space complexity analysis
* Big-O, Big-Omega, and Big-Theta notations
* Best-case, average-case, and worst-case analysis
* Backward substitution
* Master Theorem
* Recursion tree analysis
* Formal proof of asymptotic bounds
* Running-time estimation and scalability analysis

## 6. System Assumptions

The analysis follows the assumptions specified in the assessment:

* Initial product catalogue size: 100,000 products.
* Expected product catalogue size: 1,000,000 products.
* Server processing rate: 10^8 basic operations per second.
* Maximum nightly processing window: 10 minutes.

Mathematical operation counts and estimated execution times will be presented separately from any measured program execution times.

## 7. Project Structure

The project is organized into the following components:

* `README.md` – Project overview, objectives, and analysis summary.
* `algorithms/` – Algorithm implementations used to demonstrate the backend operations.
* `results/` – Operation counts, complexity comparisons, and scalability estimates.
* `report/` – Detailed assessment report containing mathematical derivations, proofs, calculations, and recommendations.

Additional files may be included when needed to support testing and presentation of results.

## 8. Expected Outcomes

The project aims to identify how the five backend modules scale as the catalogue grows. It will compare the existing recommendation engine with its proposed redesign, evaluate the searching algorithms, and determine which modules require optimization to meet the nightly processing deadline.

The final analysis will provide mathematically justified conclusions and practical recommendations for improving ShopSphere's scalability.

## 9. Conclusion

The ShopSphere Scalability Audit applies fundamental algorithm analysis techniques to a realistic e-commerce scenario. By combining theoretical complexity analysis with numerical execution-time estimates, the project aims to support informed decisions about algorithm selection, optimization, and system scalability.
