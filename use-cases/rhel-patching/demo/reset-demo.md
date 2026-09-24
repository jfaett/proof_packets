# Reset the demo

The simulation changes no managed-host state. Reset consists only of deleting generated JSON evidence.

From the repository root, inspect the target first:

~~~bash
find use-cases/rhel-patching/demo/evidence -maxdepth 1 -type f -name '*.json' -print
~~~

Then delete only those generated files:

~~~bash
find use-cases/rhel-patching/demo/evidence -maxdepth 1 -type f -name '*.json' -delete
~~~

Do not use a broad recursive deletion. Preserve any evidence intentionally retained for a review outside this disposable demonstration.
