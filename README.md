# Preliminary Research Note: Natural-Language Strategy Generation, Conversational Clarification & LLM Evaluation

**Author:** Guan Ruyue (Aiffie)  
**Project:** INERI × HKU — LLM Trader Bot  
**Date:** November 20, 2026  

---

## 1. Preferred Direction & Specific Research Question

**Preferred Direction:**  
*Models, Strategies, and Lightweight Implementation* — specifically focusing on **Natural-Language Strategy Generation**, **Conversational Refinement & Standardized Prompts**, and **LLM Model Selection & Benchmarking** (with an interface handoff to the JSON backtest schema and front-end strategy review UI).

**Specific Research Question:**  
> *In high-stakes financial trading workflows, how can a hybrid architecture combining conversational clarification and standardized schema-constrained prompting maximize logical fidelity and eliminate "silent assumptions" (e.g., ambiguous position sizing, margin modes, or missing risk controls) when translating natural-language investment ideas into executable, parameter-separated trading specifications across different LLMs (e.g., DeepSeek vs. OpenAI models)?*

---

## 2. Relevant Papers, Tools & Technical Resources

1. **Fang et al. (2026), *ClarifyCodeBench: Evaluating LLMs on Clarifying Ambiguous Requirements for Code Generation* (arXiv:2607.00711)**
   - **Key Takeaway:** Evaluates how LLMs handle underspecified requirements before generating executable outputs. Crucially, the authors find that current LLMs still struggle to detect ambiguity and tend to silently guess, and stronger general reasoning alone does not automatically improve clarification accuracy.
   - **Relevance to Project:** Directly validates our project's core requirement that *"missing or ambiguous requirements should be clarified rather than silently assumed."* We can adapt their ambiguity-injection methodology and clarification metrics to build a finance-specific benchmark.

2. **Xiao et al. (2025), *TradingAgents: Multi-Agents LLM Financial Trading Framework* (arXiv:2412.20138)**
   - **Key Takeaway:** Models real-world trading firm dynamics by separating LLM responsibilities into specialized roles (e.g., Analysts, Researchers, Traders, and a dedicated Risk Management Team), improving decision explainability and risk alignment.
   - **Relevance to Project:** Inspires separating our generation pipeline into distinct, auditable stages—*Requirement Clarification* → *Rule & Parameter Extraction* → *Risk/Constraint Validation*—rather than relying on a single unconstrained prompt.

3. **Structured Outputs (JSON Schema Constrained Decoding) & Pydantic + Binance AI Pro Case Study (Biteye / PANews, Oct 2026)**
   - **Key Takeaway:** Constrained JSON decoding paired with Pydantic validation enforces strict type, unit, and range contracts between LLM outputs and downstream engines. Meanwhile, the Binance AI Pro case highlights critical real-world execution ambiguities (e.g., whether "10% position" means notional exposure or margin allocation, margin/position modes, and stop-loss calculation basis).
   - **Relevance to Project:** Provides the engineering bridge to separate **strategy logic** from **adjustable parameters**, retain traceable revision versions, and ensure safe handoff to the backtesting module.

---

## 3. Proposed# Dissertation_llm-trader-bot-preliminary
