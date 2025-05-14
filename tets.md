## test
```
git filter-repo --force \
  --commit-callback '
    if commit.author_missing_space:
      commit.author = re.sub(r"(.*)<(.*)>", r"\1 <\2>", commit.author)
    if commit.committer_missing_space:
      commit.committer = re.sub(r"(.*)<(.*)>", r"\1 <\2>", commit.committer)
    '
```

```
git filter-branch --env-filter '
  export GIT_AUTHOR_NAME=$(echo "$GIT_AUTHOR_NAME" | sed "s/\([^<]\)</\1 </")
  export GIT_AUTHOR_EMAIL=$(echo "$GIT_AUTHOR_EMAIL" | sed "s/\([^<]\)</\1 </")
  export GIT_COMMITTER_NAME=$(echo "$GIT_COMMITTER_NAME" | sed "s/\([^<]\)</\1 </")
  export GIT_COMMITTER_EMAIL=$(echo "$GIT_COMMITTER_EMAIL" | sed "s/\([^<]\)</\1 </")
' --tag-name-filter cat -- --all
```
