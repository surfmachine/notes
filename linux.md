Linux
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# Commands


## General

Command                                | Remark
-------------------------------------- | --------------------------------------
whoami                                 | show user $(whoami) 
hostname                               | show hostname
history                                | history show
![history-number]                      | history execute command
[ctrl] [r]                             | hisotry search
cat /etc/*release                      | show version info
  

## File

Command                                | Remark
-------------------------------------- | --------------------------------------
cat [filename] \| more                 | show file content per page
sort filename.txt | uniq -d            | duplicate texte anzeigen
find ~/mydir -iname '*.htm' -exec rm {} \; | find nach file type
find ./ -name "*.jar" \| xargs grep SMTPSendFailedException.class | find Klasse in jars
find /lib* /usr/lib* -name "libgs.so" | find nach installierter Library
ldconfig -p | grep libgs.so           | find nach installierter Library
cp `ls -SF | grep -v / | head -5` [target-dir] | copy mit Resultaten aus Pipe Abfrage
  

## Permission, Owner, Groups

Command                                | Remark
-------------------------------------- | --------------------------------------
chmod 774 [filename]                   | Owner/Group=read,write,execute. Others=read
chmod -R 774 [dir]                     | Owner/Group=read,write,execute. Others=read
chown [username] [filename]            | Change Owner
chown -R [username]:[group] [dir]      | Change Owner 
groups                                 | Anzeige der aktuellen Gruppen
usermod -g [group] [user]              | Wechsel der Primary Group 


## Size matters

Command                                | Remark
-------------------------------------- | --------------------------------------
quota -v [username]                    | disk quota
df -h [directory]                      | disk available space
df -h | grep homedirs                  | disk quota's per user  
du -sh [directory]                     | disk usage (seltsame Werte?)
du -hsx * \| sort -rh                  | disk usage
du -a /var \| sort -n -r \| head -n 10 | Die 10 grössten Files / Directories im Verzeichnis /var
ls -lh                                 | file size 'user friendly'


## Jobs, Processes, Network

Command                                | Remark
-------------------------------------- | --------------------------------------
ps -fu [username]                      | show process info for the given user
ps -ef | grep tomcat                   | show process of tomcat server
ps auxwww \| grep [pid]                | show process
ps -p 13621 -o pid,vsz=MEMORY -o user,group=GROUP -o comm,args=ARGS | show process info
ip addr show                           | show ip addr
netstat -an                            | show port numbers  
[ctrl] [z] then bg                     | suspend job, then run in background
kill -3 [pid]                          | kill process mit dump
host [name]                            | dns lookup to convert name to ip address


-------------------------------------------------------------------------------
# Locations

## Linux

Location                               | Description
-------------------------------------- | --------------------------------------
.profile                               | profile settings (1)
.bashrc                                | personal settings
.bash_aliases                          | personal aliases                       
/etc/hostname                          | hostname
/etc/hosts                             | hosts, z.B. 127.0.1.1 [hostname]


(1) Use the command **source .profile** to apply new settings within the current shell. Enable the Option **Run command as login shell** within the Terminal settings to get the latest change within a new opened shell.

## Applications

Location                               | Description
-------------------------------------- | --------------------------------------
~/mavenrepo		                         | maven repo
~/.m2/settings.xml                     | maven config
~/.mavenrc                             | maven environment config (jdk)



-------------------------------------------------------------------------------
# Samples

## Text replace and sort
> cat classpath.txt | tr : \\n | sort > classpath-sorted.txt 

## SSH 
> ssh [username]@[server]


## SSH Tunnel
- tunnel : ssh -L 3000:localhost:7473 [username]@[server]
- sudo nano /etc/hosts
  127.0.0.1  [server]
- ssh -L 3000:localhost:80 [username]@[server]
- Browser: http://[url]:3000/


## SSL Show certificate from remote server
>  openssl s_client -connect [server]:[port] -showcerts

## SCP
> scp [file] [username]@[server]:[target-dir]


## Hostname Anpassen
> Anpassung hostname auf [hostname] (ist in der Datei /etc/hostname zu sehen)
> Anpassung /etc/hosts Eintrag mit 127.0.1.1 [hostname]


## Java connect to running process
> jstack [pid]

## ZIP
> zipinfo archiv/xy-0.3.0.jar | less

## Ubuntuy Unity - Reset Settings
I had the similar problem in 14.10 .  I solved it by deleting the files:

> ~/.config/dconf/user
> ~/.cache/compizconfig-1.

It worked out for me, in case if it doesn't work out for you try installing
a different window manager(in my case I had cinnamon and was able to use it
smoothly even when I had problems in default window manager).

-------------------------------------------------------------------------------
# Software

## IntelliJ
- Download ideaIU-2017.1.5.tar.gz
- Unzip nach /home/swe/work/software/idea-IU-...
- Start bin/idea.sh             // gemäss Installationsanleitung


## GIT
- sudo apt-get install git


## Visual Studio Code

### Installation via snap
- snap search "visual studio"
- snap search vscode
- snap install vscode --classic

### Remove minimap on the right side of the File  Editor
- File / Preferences / Settings:
  "editor.minimap.enabled": false

### Extensions
- Add "Markdown Preview Enhanced" by Yiyi Wang


## Ubuntu Customisation

- Tweak Tool
  > sudo apt install gnome-tweaks

- System Monitor
  > sudo apt install gnome-system-monitor

- Double File Explorer
  > sudo apt install doublecmd-gtk

## Shortcuts 

- Ctrl-Alt-D
  > Hide all windows 

- Super-H
  > Hide single window

- Super-A 
  > Show & search applications



-------------------------------------------------------------------------------
# References

- https://www.linuxmint.com/
- https://itvision.altervista.org/best-linux-distro-this-year.html
- http://www.cyberciti.biz/faq/how-do-i-find-the-largest-filesdirectories-on-a-linuxunixbsd-filesystem/ 


-------------------------------------------------------------------------------
_The end._
