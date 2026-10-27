---
title: "Lenovo Thinkbook Fedora Dock Fix"
date: 2026-10-27T11:05:27+02:00
draft: false
tags: [lenovo, thinkbook, fedora, grub, kernel, usb4]
summary: "This document describes a reproducible boot hang on a Lenovo ThinkBook 14 G7 ARP (21MV) with an AMD Ryzen 3 7335U (Radeon 680M) when connected to a Lenovo ThinkPad USB4 Dock 5000 (40BF). The system freezes at the Lenovo boot logo (Plymouth) before reaching the LUKS2 decryption prompt. The fix involves regenerating the initramfs (dracut) while the dock is connected."
translationKey: "lenovo-thinkbook-fedora-dock-fix"
---
# Fixing Fedora Boot Hang with Lenovo ThinkBook 21MV & USB4 Dock 5000 (AMD Rembrandt)


This document describes a reproducible boot hang on a Lenovo ThinkBook 14 G7 ARP (21MV) with an AMD Ryzen 3 7335U (Radeon 680M) when connected to a Lenovo ThinkPad USB4 Dock 5000 (40BF). The system freezes at the Lenovo boot logo (Plymouth) before reaching the LUKS2 decryption prompt. The fix involves regenerating the initramfs (dracut) while the dock is connected.

## Hardware & Software Environment

- Laptop: Lenovo ThinkBook 14 G7 ARP (Model 21MV)
- CPU/GPU: AMD Ryzen 3 7335U with Radeon Graphics (Rembrandt, 1002:1681)
- Dock: Lenovo ThinkPad USB4 Dock 5000 (40BF), Firmware: 1.3.00
- BIOS: Version 65574 (Lenovo)
- OS: Fedora 44 KDE Plasma (Multiboot with Windows 11)
- Kernel: 7.2.12-200.fc44.x86_64

- Storage Layout: Single NVMe drive with dual-boot:
    - Windows 11 (NTFS)
    - Fedora (BTRFS with LUKS2 encryption)
- Bootloader: GRUB2

![Partitions](partitions.jpg)


## Symptoms

- System is powered on with the USB4 dock connected.
- The Lenovo logo appears, followed by a mouse cursor.
- Keyboard and mouse are unresponsive (though NumLock LED may toggle).
- Alt+F1 (TTY switching) does not work.
- Crucially, the LUKS2 password prompt never appears because the boot process hangs earlier in the AMD GPU initialization.
- The only way to power off is to hold the dock's power button for 10 seconds.

### Log Snippet (Prior to Hang)

When booting with plymouth.enable=0 or viewing early logs, the following warning loops:

```text
amdgpu ... REG_WAIT timeout ... dcn31_program_compbuf_size
```

This indicates the AMD GPU driver is stuck waiting for a display register response, likely related to the dock's DisplayPort MST (Multi-Stream Transport) initialization.

### Root Cause

The issue is a combination of:

1. AMDGPU driver + Dock MST initialization: The GPU driver hangs when initializing the display path through the dock.

2. Stale Initramfs: The initramfs (early boot environment) was generated without the dock connected. When the kernel boots with the dock attached, the driver load order and device discovery in the early userspace do not match the actual hardware state, leading to the hang before LUKS2 can even prompt for a password.

Note: The dock's firmware (1.3.00) and the laptop's BIOS were up to date, and the dock works perfectly in Windows 11. This confirms the issue is Linux kernel/initramfs-specific.


## The Fix

Regenerate the initramfs while the USB4 dock is connected to the laptop.
```
```bash
sudo dracut --regenerate-all --force
```
**Important: Ensure the dock is plugged in and powered on during this command.**

After the command completes, reboot the system. The boot process should now proceed past the Lenovo logo, prompt for the LUKS2 password, and successfully boot into Fedora.

## Additional Notes for Dual-Boot / LUKS2 Users

- **Why the hang is critical:** Because the system hangs before the LUKS2 prompt, you cannot even enter a recovery shell or switch TTYs. The forced shutdown (10s power button) is the only option, which carries a small risk of filesystem corruption (though BTRFS is generally resilient).

- **Future kernel updates:** If you update the kernel while the dock is disconnected, you may need to run dracut --regenerate-all --force again with the dock connected to ensure the new initramfs includes the correct device topology.

- **Alternative workaround:** If you cannot regenerate the initramfs, booting with the dock disconnected and plugging it in after the LUKS prompt can serve as a temporary workaround, though hot-plugging may still trigger GPU issues.

### Verification
- uname -r → 7.2.12-200.fc44.x86_64
- fwupdmgr get-devices → Dock firmware 1.3.00
- systemctl poweroff and reboot function normally with the dock connected.