PYTHON ?= python3
ANSIBLE_PLAYBOOK ?= ansible-playbook

.PHONY: validate test syntax demo package

validate:
	$(PYTHON) scripts/validate_repository.py

test:
	$(PYTHON) -m unittest discover -s tests -v

syntax:
	@if command -v $(ANSIBLE_PLAYBOOK) >/dev/null 2>&1; then \
		$(ANSIBLE_PLAYBOOK) --syntax-check -i use-cases/rhel-patching/demo/inventory/hosts.yml use-cases/rhel-patching/demo/playbooks/rhel_patch_window.yml; \
	else \
		echo "SKIP: ansible-playbook is not installed; repository validation still ran."; \
	fi

demo:
	$(ANSIBLE_PLAYBOOK) -i use-cases/rhel-patching/demo/inventory/hosts.yml use-cases/rhel-patching/demo/playbooks/rhel_patch_window.yml

package:
	$(PYTHON) scripts/generate_shortlinks.py
