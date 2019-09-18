from flask import render_template, flash, redirect
from app import app
from app.forms import NewArtistForm


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/artists')
def artists():

    artistsList = ["Ed Sheeran","Taylor Swift","Shawn Mendes","P!nk"]

    return render_template('artists.html', title ='Artists', artists=artistsList)

@app.route('/newartist', methods=['GET', 'POST'])
def newartist():

    form = NewArtistForm()

    if form.validate_on_submit():
        flash('New Artist added: {}'.format(
            form.name.data))
        flash('Hometown: {}'.format(
            form.hometown.data))
        flash('Description: {}'.format(
            form.description.data))
        return render_template('/artist.html', name=form.name.data, hometown=form.hometown.data, description=form.description.data,)

    return render_template('newartist.html', title="New Artist", form=form, )

@app.route('/artist')
def artist():

    artistList = {
        'a1': {
            'name': "Taylor Swift",
            'hometown':'Reading, Pennsylvania',
            'description': "Taylor Swift is a singer/songwriter.  She was country now she is pop.  She just released a new album titled Lover."
        },
    }

    name = "Taylor Swift"
    hometown = "Reading, Pennsylvania"
    description = "Taylor Swift is a singer/songwriter.  She was country now she is pop.  She just released a new album titled Lover."
    return render_template('artist.html', title="Artist", artist=artistList, name=name,
                           hometown=hometown, description=description,)

@app.route('/newartistsubmit')
def newartistsubmit():

    return render_template('newartistsubmit.html', title='New Artist')