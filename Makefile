default:
	./scope_shot.py

install:
	sudo cp scope_shot.py /usr/local/bin
	sudo cp 50-oscope.rules /etc/udev/rules.d
	sudo udevadm control --reload-rules && sudo udevadm trigger

uninstall:
	sudo rm -f /usr/local/bin/scope_shot.py
	sudo rm -f /etc/udev/rules.d/50-oscope.rules
	sudo udevadm control --reload-rules && sudo udevadm trigger
