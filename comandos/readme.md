<!-- #Comandos Básicos Projeto -->
. venv/scripts/activate
python manage.py startapp contact

<!-- Comandos Git -->
eval $(ssh-agent)
ssh-add ~/.ssh/allanp_rsa

git push origin main
git pull
git commit -m ''
git add .