# 00 · Prerequisites

Do this **before** the workshop. It takes about 30 minutes. Every step ends with
a ✅ **Check** so you know it worked.

Commands go into a **terminal**:

- **macOS:** open the *Terminal* app (Cmd+Space, type "Terminal").
- **Linux:** you know where it is 🙂
- **Windows:** install Git (step 1) and use **Git Bash**, which the installer adds.
  All the commands below work in Git Bash. Where PowerShell differs, it is noted.

> Lines starting with `$` are commands you type (without the `$`). Lines without
> it are example output.

---

## 1. Install git

| OS | How |
|----|-----|
| macOS | Run `xcode-select --install`, or `brew install git` if you use Homebrew |
| Ubuntu/Debian | `sudo apt update && sudo apt install git` |
| Windows | Download from <https://git-scm.com/download/win> and keep the default options. This also installs **Git Bash** |

✅ **Check:**

```console
$ git --version
git version 2.4x.x
```

## 2. Install Python 3.10 or newer

| OS | How |
|----|-----|
| macOS | `brew install python`, or the installer from <https://www.python.org/downloads/> |
| Ubuntu/Debian | `sudo apt install python3 python3-venv python3-pip` |
| Windows | Installer from <https://www.python.org/downloads/>. ⚠️ Tick **"Add python.exe to PATH"** |

✅ **Check:** `python3 --version` (on Windows: `python --version`) prints 3.10 or newer.

## 3. Create a GitHub account

Sign up at <https://github.com/signup>. Pick a professional username, because
you'll use it for years.

💡 **Students:** apply for the free **GitHub Student Developer Pack** at
<https://education.github.com/pack> with your `@studenti.polito.it` email.

## 4. Tell git who you are

Git stamps every commit with a name and email. Use the **same email as your
GitHub account** so GitHub can link commits to you.

```bash
git config --global user.name "Name Surname"
git config --global user.email "you@example.com"

# Call the first branch "main" (the modern default)
git config --global init.defaultBranch main

# When you `git pull` into a branch that has your own commits, merge
# (without this, newer git versions stop and ask you every time)
git config --global pull.rebase false

# Use an editor you know for commit messages (pick ONE line)
git config --global core.editor "nano"          # simple terminal editor
git config --global core.editor "code --wait"   # VS Code
```

> 😱 **Stuck in a strange editor after `git commit`?** That's probably **vim**.
> Press `Esc`, type `:wq`, and press `Enter` to save and quit. Then set
> `core.editor` as shown above.

**Windows only:** make git handle line endings for you:

```bash
git config --global core.autocrlf true
```

✅ **Check:**

```console
$ git config --global --list
user.name=Name Surname
user.email=you@example.com
init.defaultbranch=main
...
```

### 4b. Set up a global ignore file

Your editor and OS create junk files (`.DS_Store`, `.vscode/`, `.idea/`, `*.swp`)
that must never end up in a repo. Set up a **personal ignore file** once, and it
protects you in every repository. Follow
**[gitignore-guide.md → section 3](gitignore-guide.md#3--two-kinds-of-ignore-files-project-vs-personal)**.
It takes about 2 minutes.

## 5. Create an SSH key and add it to GitHub

### Why?

When git talks to GitHub, GitHub needs to know it's really you. An **SSH key**
is a pair of files:

- a **private key** (`id_ed25519`) that **never leaves your computer**. Never share it.
- a **public key** (`id_ed25519.pub`) that you give to GitHub. It is safe to share.

Once GitHub has your public key, you can push and pull without typing a password.

### 5.1 Check if you already have a key

```bash
ls ~/.ssh
```

If you see `id_ed25519` and `id_ed25519.pub`, you already have a key. Skip to **5.4**.
If you get "No such file or directory" or don't see those files, continue.

### 5.2 Generate a new key

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

- **"Enter file in which to save the key"**: press `Enter` to accept the default.
- **"Enter passphrase"**: type a passphrase (recommended) or press `Enter` for none.
  Nothing appears while you type. That's normal.

### 5.3 Add the key to the SSH agent

The agent remembers your passphrase so you don't type it every time.

<details>
<summary><b>macOS</b></summary>

```bash
eval "$(ssh-agent -s)"
```

Create (or edit) the file `~/.ssh/config`:

```bash
touch ~/.ssh/config
open -e ~/.ssh/config
```

and paste:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Save, then run:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
</details>

<details>
<summary><b>Linux</b></summary>

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
</details>

<details>
<summary><b>Windows (Git Bash)</b></summary>

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you'd rather use **PowerShell as Administrator** so the agent starts automatically:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```
</details>

### 5.4 Copy your **public** key

| OS | Command |
|----|---------|
| macOS | `pbcopy < ~/.ssh/id_ed25519.pub` |
| Windows (Git Bash) | `clip < ~/.ssh/id_ed25519.pub` |
| Windows (PowerShell) | `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub \| Set-Clipboard` |
| Linux | `cat ~/.ssh/id_ed25519.pub`, then select and copy the output |

It looks like this (one single line):

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA...a-long-string... you@example.com
```

⚠️ Make sure you copy the file ending in **`.pub`**.

### 5.5 Add it to GitHub

1. GitHub → click your profile picture (top right) → **Settings**
2. Left sidebar → **SSH and GPG keys** → **New SSH key**
3. **Title:** something like `MacBook Can` · **Key type:** Authentication Key
4. Paste the key into **Key** → **Add SSH key**

### 5.6 Test the connection

```bash
ssh -T git@github.com
```

The first time, you'll see:

```
The authenticity of host 'github.com (...)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Check that the fingerprint matches **GitHub's published fingerprints**
(<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints>),
then type `yes`.

✅ **Check:**

```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

That message means it **worked** 🎉. The "does not provide shell access" part is normal.

### Troubleshooting SSH

| Problem | Fix |
|---------|-----|
| `Permission denied (publickey)` | The key isn't on GitHub or isn't loaded. Re-run `ssh-add ~/.ssh/id_ed25519` and check step 5.5. `ssh -vT git@github.com` shows details |
| `Connection timed out` / `Connection refused` on port 22 | Some networks (university Wi-Fi, eduroam, some hotspots) block port 22. Use port 443 instead, see below |
| You pasted the private key | Delete it from GitHub immediately, then generate a new key pair |

**Using SSH over port 443.** Add this to `~/.ssh/config`:

```
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```

Then run `ssh -T git@github.com` again.

## 6. Clone a repository

**Cloning** downloads a copy of a repository, including its entire history, to
your computer.

1. Open the repository on GitHub, for example <https://github.com/H2politO/git-workshop>
2. Click the green **`<> Code`** button → **SSH** tab → copy the URL
   (it looks like `git@github.com:H2politO/git-workshop.git`)
3. In the terminal, go to the folder where you keep projects and clone:

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:H2politO/git-workshop.git
cd git-workshop
```

> ⚠️ Pick the **SSH** URL (`git@github.com:...`), not HTTPS (`https://...`).
> HTTPS asks for a token every time. If you already cloned with HTTPS, switch it with:
> `git remote set-url origin git@github.com:OWNER/REPO.git`

> 📝 **During the workshop you'll clone your *fork* instead** (Exercise 1).
> Cloning the original now is just to test that everything works. You can delete
> this folder afterwards.

## 7. Run the program

Inside the `git-workshop` folder:

```bash
python3 -m ecotrack data/sample_laps.csv     # Windows: python -m ecotrack data/sample_laps.csv
```

✅ **Check:** you see something like

```
Total time:   32:51.92
Best lap:     4:2.71
Average lap:  4:6.49
```

(Yes, `4:2.71` looks odd. That's a bug you'll fix during the workshop 😉)

## ✅ You're ready!

- [ ] `git --version` works
- [ ] `git config --global user.name` and `user.email` are set
- [ ] `~/.config/git/ignore` exists with the blocks for your OS and editor
- [ ] `ssh -T git@github.com` says "Hi *username*!"
- [ ] You cloned the repo with an SSH URL
- [ ] `python3 -m ecotrack data/sample_laps.csv` prints the lap summary

See you at the workshop! 🚀
