# Async Web Scraper

This project is a small, focused exploration of **asynchronous I/O and concurrency in Python**.

The goal is not to build a production-grade scraper, but to understand:
- how async tasks are scheduled
- how concurrency limits work using semaphores
- how deterministic result ordering can be preserved even when requests complete out of order

---

## What This Project Does

1. Collects URLs from a base webpage (synchronously).
2. Launches asynchronous HTTP requests for all collected URLs.
3. Limits the number of in-flight requests using an asyncio semaphore.
4. Fetches all URLs concurrently using `httpx.AsyncClient`.
5. Returns results in **input order**, regardless of completion order.

---

## Why Async Instead of Threads?

This project focuses on **I/O-bound concurrency**.

Network requests spend most of their time waiting. Async allows the event loop to switch between tasks efficiently without the overhead of threads.

---

## Key Design Decisions

### 1. Task-Based Concurrency (No Worker Queue)

All URLs are known upfront, so tasks are created in a single batch.
A queue is intentionally not used, as there is no producer–consumer overlap.

### 2. Concurrency Control via Semaphore

A semaphore limits the number of simultaneous HTTP requests, preventing resource exhaustion.

### 3. Deterministic Ordering

Although requests complete out of order, results are returned in input order using `asyncio.gather`, which preserves task ordering.

---

## Project Structure

async-web-scraper/
├── url_manager.py # Collects and normalizes URLs from a base page
├── orchestrator.py # Orchestrates async tasks and concurrency control
├── requirements.txt # dependencies
├── .gitignore
└── README.md 

---

## Example Behavior

When running the scraper, you might see logs like:

fetching started for url id:0
fetching started for url id:1
fetching started for url id:2
fetching completed for url id:1
fetching completed for url id:0
fetching completed for url id:2

Even though requests complete out of order, the final results are returned in the order of the input list.

---

## Limitations

This project is **intentionally simple**. It does **not** include:
- Retry logic for failed requests
- Rate limiting for each domain
- Persistent storage
- Streaming URL discovery or dynamic queueing

These omissions are deliberate to focus **async fundamentals**.

---

## Possible Extensions

If you want to expand the project in the future, you could add:
- Async queues for streaming URL ingestion (like a worker-queue, current is mostly task-based)
- Retry and timeout policies per request
- Domain-based rate limiting
- Storing results to a databasdbe or CSV file

---
Install dependencies:

```bash
pip install -r requirements.txt


