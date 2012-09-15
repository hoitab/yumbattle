'''
Created on 15 Sep 2012

@author: hoi
'''
import logging
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import blobstore_handlers
from model.meal import Meal

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):

    def post(self):

        logging.info('Starting PhotoUploadHandler')

#        try:
        picture_file = self.get_uploads('picture')
        logging.info('Getting picture file')
        location = self.request.get('canteenLocation')
        logging.info('Upload photo is from (%s)', location)

        meal = Meal(picture='Placeholder picture', # picture_file.key(),
            canteenlocation=location,
            canteenid='Placeholder ID',
            canteenname='Placeholder Name',
            contestcount = 0,
            contestscore = 0)
        logging.info('Meal object created')

        db.put(meal)
        logging.info('Meal object stored')

#        except:
#            logging.info('Error uploading picture')


application = webapp.WSGIApplication([('/uploadphoto', PhotoUploadHandler)
                                     ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
