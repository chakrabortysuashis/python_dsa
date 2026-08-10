---
name: dsa-explain
description: Explain Data Structures and Algorithms concepts in Python files using the dsa_teacher agent. Trigger this skill when you want detailed explanations, dry-run traces, step-by-step walkthroughs, or edge case analysis of DSA code. The skill reads the target file, invokes the dsa_teacher agent to provide comprehensive explanations, and embeds the explanations directly within the file as comments or annotations. Use this when studying algorithms, preparing for interviews, or needing to understand complex DSA implementations.
---
# DSA Explain Skill

This skill provides detailed explanations of Data Structures and Algorithms concepts in Python files by leveraging the specialized dsa_teacher agent.

## When to Use

- You want to understand how a specific DSA algorithm works
- You need step-by-step execution traces of algorithms
- You want edge cases highlighted and explained
- You're studying for technical interviews and need deeper insights
- You want visual explanations of data structure operations
- You need complexity analysis explained in detail

## How It Works

When you invoke `/dsa-explain <file_path>`, the skill:

1. Reads the specified Python file containing DSA code
2. Invokes the dsa_teacher agent with the file content
3. The dsa_teacher agent analyzes the code and provides:
   - Detailed explanations of each section
   - Step-by-step dry-run traces with sample inputs
   - Visual representations of data structure changes
   - Edge case analysis
   - Time and space complexity explanations
   - Alternative approaches and trade-offs
4. The explanations are embedded directly within the file as inline comments or block comments
5. The modified file is saved with explanations preserved

## Usage

Invoke the skill with:
```
/dsa-explain <path_to_python_file>
```

Examples:
```
/dsa-explain Two_Pointers/_02_longest_substring_without_repeat_chars.py
/dsa-explain Arrays/_01_two_sum_sortedarray.py
```

## Expected Output

The skill will modify the target file to include comprehensive explanations while preserving the original code. Explanations are added as:
- Block comments before functions/classes explaining purpose and approach
- Inline comments on complex lines explaining the logic
- Special comment markers for dry-run traces and visual explanations
- Complexity analysis sections
- Edge case handling explanations

## Requirements

- The target file must be a Python (.py) file containing DSA implementations
- The dsa_teacher agent must be available in the environment
- Write permissions to modify the target file

## Notes

- Original code is preserved; only explanatory comments are added
- Explanations are designed to be educational and interview-focused
- The skill works best with well-structured DSA implementations
- For very large files, consider explaining specific functions or sections separately