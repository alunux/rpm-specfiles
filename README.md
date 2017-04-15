# rpm-specfiles
My RPM spec files for Fedora

**How to use:**
- Prepare development tools: `$ sudo dnf install gcc git rpmdevtools`
- Setup RPM build tree: `$ rpmdev-setuptree`
- Clone this git repo: `$ git clone https://github.com/alunux/rpm-specfiles.git && cd rpm-specfiles`
- Copy spec file which you want to build, for example budgie-desktop-git: `$ cp budgie-desktop-git.spec ~/rpmbuild/SPECS`
- Enter ~/rpmbuild/SPECS directory: `$ cd ~/rpmbuild/SPECS`
- Install all build requirements: `$ sudo dnf builddep budgie-desktop-git.spec`
- Build the package: `$ rpmbuild -bb budgie-desktop-git.spec`
- When done, you’ll see the binary RPM in the ~/rpmbuild/RPMS directory:


**For Copr repo, visit:** https://copr.fedorainfracloud.org/coprs/alunux
