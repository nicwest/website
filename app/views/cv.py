from flask import Flask, render_template
from app import app, db, models


@app.route('/cv')
def cv_display_temp():
    return render_template('temp_cv.html')

@app.route('/cv/<slug>')
def cv_display(slug):
    cv = models.CV.query.filter_by(slug=slug).first()
    items = [x.item for x in cv.items.order_by(models.CVItem.order.asc()).all()]
    return render_template('cv_template.html', cv=cv, items=items)



