# Github Action for Liquibase

This action is designed to simplify and speed up Liquibase processes.

## Code structure
```bash
ccdevops_shared_liquibase_action
├ .github 
   ├ 
    workflows
    └── update.yml            
└── README.md
```

### **update.yml**

**Description:** This YAML file is the configuration for your GitHub workflow. It defines metadata about the workflow, such as name, author, description, inputs, outputs, and how the action is performed.

**Input variables** 

Name                | Description                                               | Type
---                 | ---                                                       | ---
changelogFile       | Name of the changelog file                                | String


**Steps:** 

Action                  | Verified Action               | Action Version
---                     | :---:                         | :---:
Checkout                | &check;                       | v4
Run update              | &check;                       | v4.23.2


## Usage

**Note:** You need to replace **nodejs-version** with the NodeJS version of your application.
```bash
-   name: Run Update
    uses: GitHub-EDP/ccdevops_shared_liquibase_action/.github/workflows/update.yml@main
    with:
        changelogFile: "example.sql"
```