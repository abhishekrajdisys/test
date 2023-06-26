Testing only
adding one moremain branch

git push -u origin main, you are pushing your local main branch to the remote repository and setting it as the upstream branch. This enables you to easily push future changes to the origin remote by simply running git push without specifying the branch and remote.


git clone <https://name-of-the-repository-link>

git branch <branch-name>

git push -u <remote> <branch-name>

git branch or git branch --list

git checkout <name-of-your-branch>


git checkout -b <name-of-your-branch>

git status

git pull <remote>


today i created rough .yaml file for CI/CD deployement .COnfigured test file .Then leanrt refresh about git concept and testing concept which help in deploying tomorrow.Tomorrrow we will deploy whole CI/CD pipeline with github actions.


echo "# python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/abhishekrajdisys/python.git
git push -u origin main