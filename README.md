# 📚 GradeBook — Team Python & Git Exercise

A simple student grade management system to build together as a team.

---

## 🎯 Goal

Complete 10 Python functions spread across 3 modules, using a proper Git workflow.
Each function is marked with `# TODO` and raises `NotImplementedError` until implemented.

---

## 🗂️ Project structure

```
gradebook/
├── README.md
├── students.py      # Student management       → Developer A
├── grades.py        # Grade calculations        → Developer B
├── reports.py       # Reporting & summaries     → Developer C
├── main.py          # Demo runner (shared)
└── tests.py         # Manual test cases (shared)
```

---

## 👥 Task assignment (group of 3)

| Developer | File | Functions |
|-----------|------|-----------|
| **Dev A** | `students.py` | `add_student`, `remove_student`, `find_student` |
| **Dev B** | `grades.py` | `add_grade`, `get_average`, `get_subjects`, `get_failing_students` |
| **Dev C** | `reports.py` | `get_top_students`, `summarize_class`, `export_report` |

> For groups of 4: Dev D helps Dev A and takes `find_student` + improves `main.py`.

---

## 🔀 Git workflow rules

1. **No direct push to `main` or `develop`** — ever.
2. Each dev works on their own branch: `feature/students`, `feature/grades`, `feature/reports`.
3. Every merge into `develop` requires a **pull request** reviewed by at least one teammate.
4. Use **interactive rebase** (`git rebase -i`) to clean up your commits before opening a PR.
5. After all features are merged into `develop`, the team lead opens one final PR to merge `develop` → `main` and tags it `v1.0`.

### Suggested commit message format
```
feat: implement add_student function
fix: handle duplicate student_id in add_student
refactor: simplify average calculation logic
```

---

## 🚀 Getting started

```bash
# 1. One team member creates the repo on GitHub and adds the others as collaborators.
# 2. Everyone clones it.
git clone <your-repo-url>
cd gradebook

# 3. Create the shared develop branch.
git switch -c develop
git push origin develop

# 4. Each dev creates their feature branch from develop.
git switch develop
git switch -c feature/students   # Dev A
git switch -c feature/grades     # Dev B
git switch -c feature/reports    # Dev C

# 5. Work, commit, push, open PR.
git add students.py
git commit -m "feat: implement add_student and remove_student"
git push origin feature/students
```

---

## ✅ Definition of done

- [ ] All 10 functions implemented and no `NotImplementedError` raised
- [ ] `tests.py` runs without errors
- [ ] Each function has a clean, readable implementation
- [ ] Git history is clean (no "WIP", "fix fix", "oops" commits on `develop`)
- [ ] A `v1.0` tag exists on `main`
