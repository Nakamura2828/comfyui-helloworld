# Git Quick Reference for ComfyUI Development

## Daily Workflow

```bash
# Start work session
git pull                          # Get latest from GitHub
git checkout -b feature-name      # New feature branch

# While working
git status                        # See what changed
git diff                          # See changes in detail
git add .                         # Stage all changes
git commit -m "Description"       # Commit

# Finish feature
git checkout main                 # Back to main
git merge feature-name            # Merge in your feature
git push                          # Send to GitHub
git branch -d feature-name        # Clean up branch
```

## When Things Go Wrong

```bash
# Undo unstaged changes
git checkout -- filename.py       # Discard changes to one file
git reset --hard                  # Discard ALL unstaged changes (DANGEROUS!)

# Undo staged changes
git reset HEAD filename.py        # Unstage one file
git reset                         # Unstage everything

# Fix last commit
git commit --amend -m "New msg"   # Change commit message
git add forgotten.py              # Stage forgotten file
git commit --amend --no-edit      # Add to last commit

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1           # DANGEROUS!

# Abort a merge
git merge --abort

# Save work temporarily
git stash                         # Save and clear working dir
git stash pop                     # Restore saved work
```

## Inspecting History

```bash
# View commits
git log --oneline --graph         # Pretty log
git log -p                        # With diffs
git log --author="Name"           # By author
git log -- filename.py            # For one file

# Compare things
git diff                          # Unstaged changes
git diff --cached                 # Staged changes
git diff main feature             # Between branches
git diff HEAD~3 HEAD              # Last 3 commits

# Find who changed what
git blame filename.py             # Line-by-line history
```

## Branches

```bash
# List branches
git branch                        # Local branches
git branch -a                     # Include remote branches

# Create and switch
git checkout -b new-branch        # Create and switch
git checkout existing-branch      # Switch to existing

# Delete branches
git branch -d branch-name         # Delete local
git push origin --delete branch   # Delete remote
```

## Working with GitHub

```bash
# First time setup
git remote add origin URL         # Connect to GitHub
git push -u origin main           # First push

# Regular pushes
git push                          # Send commits to GitHub
git pull                          # Get updates from GitHub

# Check remote
git remote -v                     # See remote URLs
```

## .gitignore Patterns

```bash
# Patterns
*.log                             # All .log files
temp/                             # Directory
!important.log                    # Exception (don't ignore)
**/cache/                         # Any cache/ dir anywhere

# Test what's ignored
git check-ignore -v file.txt      # Why is this ignored?
git status --ignored              # Show ignored files
```

## Emergency Commands

```bash
# Lost commits (within ~30 days)
git reflog                        # Show all HEAD movements
git reset --hard abc123           # Restore to that commit

# Corrupted repository
git fsck                          # Check for issues

# Clean up
git clean -fd                     # Remove untracked files (DANGEROUS!)
git gc                            # Garbage collection
```

## Best Practices

1. **Commit often** - Small, focused commits
2. **Write good messages** - Future you will thank you
3. **Branch for features** - Keep main stable
4. **Pull before push** - Avoid conflicts
5. **Test before commit** - Run tests first!
6. **Review before staging** - `git diff` is your friend

## Common Mistakes to Avoid

❌ `git add .` without reviewing
✅ `git diff` then `git add` specific files

❌ Committing secrets/passwords
✅ Use `.env` files in `.gitignore`

❌ Working directly on main
✅ Use feature branches

❌ `git push --force` on shared branches
✅ Only force push on your own branches

❌ Huge commits with mixed changes
✅ One logical change per commit
