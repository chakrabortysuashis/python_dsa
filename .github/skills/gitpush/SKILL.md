---
name: gitpush
description: Automate git commit and push process with intelligent commit message generation. Use when you want to quickly commit changes and push to remote repository. Takes an optional description parameter for commit message. Handles checking status, generating commit messages, pulling changes, and pushing to current branch.
---

# GitPush Skill

This skill automates the git commit and push process with intelligent commit message generation.

## When to Use

Use this skill when you want to:
- Quickly commit staged/unstaged changes and push to remote repository
- Automate the git workflow with intelligent commit message generation
- Handle the full commit-pull-push cycle in one command
- Get descriptive output showing each step of the process

## Parameters

- `description` (optional): Custom commit message to use instead of auto-generated one

## Steps

Follow these steps when executing the `/gitpush` command:

1. **Check git status**
   - Run `git status --porcelain` to see staged and unstaged changes
   - If no changes detected, output "No changes to commit" and exit

2. **Determine commit message**
   - If `description` parameter is provided, use it as commit message
   - If no description provided:
     - Analyze the changes from git status to determine commit objective
     - Generate a concise, descriptive commit message following conventional commit format when possible
     - Example formats: "feat: add new feature", "fix: resolve issue", "docs: update documentation", etc.

3. **Execute git commit**
   - Run `git add -A` to stage all changes
   - Run `git commit -m "<commit_message>"` with the determined message
   - If commit fails (e.g., no changes after staging), handle gracefully

4. **Execute git pull**
   - Run `git pull` to check for and incorporate incoming changes
   - If merge conflicts occur, output conflict information and stop before pushing
   - User must resolve conflicts manually before retrying

5. **Get current branch**
   - Run `git branch --show-current` to get the current branch name
   - If that fails, fall back to `git rev-parse --abbrev-ref HEAD`

6. **Execute git push**
   - Run `git push origin <branch_name>` to push to the remote repository
   - If push fails due to authentication or other issues, output error details

## Edge Cases Handled

- **No changes**: Skill detects when there are no staged or unstaged changes and exits early
- **Not in git repository**: If not in a git repo, outputs error and exits
- **Merge conflicts**: During pull, if conflicts are detected, skill stops and instructs user to resolve manually
- **Push failures**: Reports authentication errors, network issues, or other push problems
- **Commit failures**: Handles cases where commit might fail after staging

## Expected Output

The skill provides informative output showing:
- Detected changes (if any)
- Generated or provided commit message
- Results of git commit, pull, and push operations
- Any errors encountered during the process

## Examples

```
/gitpush
```
- Automatically detects changes, generates commit message, commits, pulls, and pushes

```
/gitpush "Fix login button alignment issue"
```
- Uses provided commit message, then commits, pulls, and pushes

## Requirements

- Must be run within a git repository
- Requires git to be installed and accessible in PATH
- Remote repository must be configured (origin remote)