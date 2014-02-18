from app import db, models
import datetime

#drop previous database (uncomment for testing)
print "Dropping previous tables..."
#db.drop_all()

#create tables
print "Creating tables from models..."
db.create_all()

#long text
overview_text = "Design graduate with 3 years experience of creating complex ebooks and enhanced picture books for \
various publishing clients. Winner of the 2013 Publishing Innovation Award for Best Ebook at the Digital Book \
World Conference for Random House UK."

github_subtitle = """Source code is availble at <a href="http://github.com/nicwest/website">github.com/nicwest/\
website</a>. Feel free to <i class="fa fa-code-fork"></i>!<br/>
Copyright &copy; 2014 Nic West"""

#add default CV
print "Adding Default CV..."
cv = models.CV(title="Default", slug="default")

db.session.add(cv)
db.session.commit()

#add default categories
print "Adding Default Categories..."
overviews = models.Item('category', '', 'Overviews', key='overview', default_order=0)
history = models.Item('category', 'History', 'History', key='history', icon="fa-clock-o", default_order=1)
skills = models.Item('category', 'Skills', 'Skills', key='skills', icon="fa-magic", default_order=2)
expertise = models.Item('category', 'Expertise', 'Expertise', key='expertise', icon="fa-bullseye", default_order=3)
work = models.Item('category', 'Work Examples', 'Work Examples', key='work', icon="fa-cogs", default_order=4)
me = models.Item('category', 'Me', 'Personal Information', key='me', icon="fa-user", default_order=5)
github = models.Item('category', 'This', 'Github', key='github', icon="fa-github", note=github_subtitle, default_order=6)

db.session.add(overviews)
db.session.add(history)
db.session.add(skills)
db.session.add(expertise)
db.session.add(work)
db.session.add(me)
db.session.add(github)

db.session.commit()

db.session.add(models.CVItem(cv, overviews, overviews.default_order, all_children=True))
db.session.add(models.CVItem(cv, history, history.default_order, all_children=True))
db.session.add(models.CVItem(cv, skills, skills.default_order, all_children=True))
db.session.add(models.CVItem(cv, expertise, expertise.default_order, all_children=True))
db.session.add(models.CVItem(cv, work, work.default_order, all_children=True))
db.session.add(models.CVItem(cv, me, me.default_order, all_children=True))
db.session.add(models.CVItem(cv, github, github.default_order, all_children=True))

db.session.commit()

#add default overview
print "Adding Default Overview..."
overview = models.Item('subheader', 'Overview', 'Overview', key='overview', parent=overviews)
db.session.add(overview)
db.session.add(models.Item('single-left', overview_text, 'Publishing Overview',  key='overview', parent=overview))
db.session.commit()

#add default history
print "Adding Default History..."
history_subs = [
    models.Item('subheader', 'Experience',  'Experience',   key='experience', parent=history, default_order=0),
    models.Item('subheader', 'Education',  'Education',   key='education', parent=history, default_order=1),
    models.Item('subheader', 'Qualifications',  'Qualifications',   key='qualifications', parent=history, default_order=2),
    models.Item('subheader', 'Awards',  'Awards',   key='awards', parent=history, default_order=3),
]
history_data = [
    models.Item('period',
                """<strong>Digital Director (Founder)</strong> @ <strong>Stunjelly</strong><br />
Stunjelly is a Digital publishing consultancy that specializes in complex
EPUB/MOBI, creation, corrections and conversions.<br/>
<a href="http://stunjelly.com">stunjelly.com</a>""",
                "Stunjelly (2010 - Present)",
                key="2010 - Present", parent=history_subs[0], default_order=0),
    models.Item('period',
                """<strong>Web Development Assistant</strong> @ <strong>Random House</strong><br/>
Short term contract for in house tool build""",
                "Random House (Jul - Aug 2010)",
                key="Jul - Aug 2010", parent=history_subs[0], default_order=1),
    models.Item('period',
                """<strong>Digital Assistant</strong> @ <strong>Random House</strong><br/>
Short term contract for server migration""",
                "Random House (Dec - Jan 2009/10)",
                key="Dec - Jan 2009/10", parent=history_subs[0], default_order=2),
    models.Item('period',
                """<strong>Assistant Climbing Instructor</strong> @ <strong>Westway Sports center</strong><br />
Weekend and vacation work supervising/coaching children and adults in indoor rock climbing.""",
                "Westway (2004 - 2006)",
                key="2004 - 2006", parent=history_subs[0], default_order=3),
    models.Item('period',
                """<strong>Student</strong> @ <strong>Leeds College of Art.</strong>""",
                "Student (Leeds)",
                key="2007 - 2010", parent=history_subs[1], default_order=0),
    models.Item('period',
                """<strong>Design Scholar</strong> @ <strong>Bedales School Hampshire</strong>""",
                "Design Scholar (Bedales)",
                key="2005 - 2006", parent=history_subs[1], default_order=1),
    models.Item('period',
                """<strong>BA(Hons) Three Dimensional Design</strong> (2nd class)""",
                "BA(hons) 3d Design",
                key="University", parent=history_subs[2], default_order=0),
    models.Item('period',
                """<strong>Maths:</strong> B, <strong>Physics</strong> B, <strong>Design</strong> B,
<strong>Chemistry</strong> C""",
                "A-Levels",
                key="A-Level", parent=history_subs[2], default_order=1),
    models.Item('period',
                """<strong>Publishing Innovation Award for Best Ebook</strong><br/><em>Dinosaur that Pooped Christmas</em> (Random House UK)<br/><a href="http://www.randomhouse.co.uk/news/2013/01/the-dinosaur-that-pooped-christmas-wins-publishing-innovation-award">http://www.randomhouse.co.uk/news/2013/01/the-dinosaur-that-pooped-christmas-wins-publishing-innovation-award</a>""",
                "Publishing Inovation Award",
                key="2013", parent=history_subs[3], default_order=0),
    models.Item('period',
                """<strong>GIDE Student Design Award</strong><br/><em>Group for International Design Education</em>
(Switzerland)</div>""",
                "GIDE",
                key="2010", parent=history_subs[3], default_order=1)
]

for item in history_subs:
    db.session.add(item)

db.session.commit()

for item in history_data:
    db.session.add(item)

db.session.commit()

#add default skills
print "Adding Default Skills..."
skills_subs = [
    models.Item('subheader', 'Programming', 'Programming', key='programming', parent=skills, default_order=0),
    models.Item('subheader', 'Frameworks', 'Frameworks', key='framesworks', parent=skills, default_order=1),
    models.Item('subheader', 'API\'s', 'API\'s', key='apis', parent=skills, default_order=2),
    models.Item('subheader', 'OS\'s', 'OS\'s', key='oss', parent=skills, default_order=3),
    models.Item('subheader', 'Programs', 'Programs', key='programs', parent=skills, default_order=4),
    models.Item('subheader', 'Other', 'Other', key='skills_other', parent=skills, default_order=5),
]
skills_data = [
    models.Item('bar', 9, "HTML5", key="HTML5", parent=skills_subs[0], default_order=0),
    models.Item('bar', 9, "CSS3", key="CSS3", parent=skills_subs[0], default_order=1),
    models.Item('bar', 8, "Javascript", key="Javascript", parent=skills_subs[0], default_order=2),
    models.Item('bar', 7, "Python", key="Python", parent=skills_subs[0], default_order=3, note="Python 2.7 (some 3.3 experience)"),
    models.Item('bar', 6, "PHP", key="PHP", parent=skills_subs[0], default_order=4),
    models.Item('bar', 5, "Perl", key="Perl", parent=skills_subs[0], default_order=5),
    models.Item('bar', 4, "Ationscript3", key="Ationscript3", parent=skills_subs[0], default_order=6),
    models.Item('bar', 2, "C/C++", key="C/C++", parent=skills_subs[0], default_order=7),

    models.Item('bar', 9, "EPUB", key="EPUB", parent=skills_subs[1], default_order=0),
    models.Item('bar', 8, "jQuery", key="jQuery", parent=skills_subs[1], default_order=1),
    models.Item('bar', 6, "Flask", key="Flask", parent=skills_subs[1], default_order=2),
    models.Item('bar', 6, "Bootstrap", key="Bootstrap", parent=skills_subs[1], default_order=3),
    models.Item('bar', 5, "Wordpress", key="Wordpress", parent=skills_subs[1], default_order=4),
    models.Item('bar', 4, "Django", key="Django", parent=skills_subs[1], default_order=5),
    models.Item('bar', 3, "Node.js", key="Node.js", parent=skills_subs[1], default_order=6),

    models.Item('bar', 7, "Twitter", key="Twitter", parent=skills_subs[2], default_order=0),
    models.Item('bar', 5, "Facebook", key="Facebook", parent=skills_subs[2], default_order=1),

    models.Item('bar', 7, "Linux", key="Linux", parent=skills_subs[3], default_order=0),
    models.Item('bar', 6, "Windows", key="Windows", parent=skills_subs[3], default_order=1),
    models.Item('bar', 5, "Android", key="Android", parent=skills_subs[3], default_order=2),
    models.Item('bar', 4, "iOS", key="iOS", parent=skills_subs[3], default_order=3),
    models.Item('bar', 3, "OSx", key="OSx", parent=skills_subs[3], default_order=4),

    models.Item('single-left', "GIMP, EpubCheck, Sigil, Pycharm, Sublime Text, Photoshop, Dreamweaver, Illustrator, \
    Fireworks, MS Office, Libre Office, MySQL Workbench", "Programs General",
                parent=skills_subs[4], default_order=0),

    models.Item('single-left', "XMPP, OpenId, IRC, ImageMagick, GD, PIL, Qt4, PDO, MySQL, SQLite, PostgreSQL, MSSQL, \
    JSON, Heroku, AWS, Redis, SocketIO, Git, OpenGL, Apache, WSGI, Restful API's", "Programs General",
                parent=skills_subs[5], default_order=0),
]

for item in skills_subs:
    db.session.add(item)

db.session.commit()

for item in skills_data:
    db.session.add(item)

db.session.commit()

#add default expertise
print "Adding Default Expertise..."
expert_list = models.Item('list-icon', '', 'Expertise List', parent=expertise)

db.session.add(expert_list)
db.session.commit()

expertise_data = [
    models.Item('list-icon-item', "strong out of the box and creative thinker. Quick to grasp situations and concepts.\
    Reasonably used to cross referencing ideas with reality and past experience. Not afraid to take educated guesses.",
                'Concepts', key='Concepts', parent=expert_list, default_order=0, icon="fa-lightbulb-o"),
    models.Item('list-icon-item', "three years experience handling multiple projects for multiple clients. \
    Good at working to deadlines and milestones. Good at automating tasks to maximise output.",
                'Time Management', key='Time Management', parent=expert_list, default_order=1, icon="fa-clock-o"),
    models.Item('list-icon-item', "works well autonomously or as part of team. Experience working as part of both small\
     and large teams, both in the real world and digitally. Experience both as a freelancer and managing sub-\
    contractors.",
                'Teams', key='Teams', parent=expert_list, default_order=2, icon="fa-users"),
    models.Item('list-icon-item', "extensive knowledge of eBook production. Experience of working with over two \
    thousand problematic or complex titles. Excellent understanding of how books render on a large range of devices. \
    Well versed in multiple mainstream reseller's guidelines and requirements (including Amazon, Apple and Barnes and \
    Noble). Creative enhancement producer. Passionate about this technology and the implications for going forwards.",
                'eBooks', key='eBooks', parent=expert_list, default_order=3, icon="fa-book"),
    models.Item('list-icon-item', "Actively enjoys hunting down and fixing problems in both his and other peoples code.\
     Enjoys the satisfaction of seeing something that is broken or not working correctly restored to working order. \
    Good at working in mediums that are unsubjective in their results.",
                'Bug Squishing', key='Bug Squishing', parent=expert_list, default_order=4, icon="fa-bug"),
    models.Item('list-icon-item', "Connected since an early age. Rarely disconnected. Fanatical about almost anything \
    that allows him to stay connected.",
                'Web Native', key='Web Native', parent=expert_list, default_order=5, icon="fa-globe"),
    models.Item('list-icon-item', "Linux (Ubuntu and Mint) used at home and in the office. Experience with Linux based \
    web servers. Far more at home with terminals than GUI's. Terrible at VIM.",
                'Linux Enthusiastically', key='Linux Enthusiastically', parent=expert_list, default_order=6,
                icon="fa-linux"),
]

for item in expertise_data:
    db.session.add(item)

db.session.commit()