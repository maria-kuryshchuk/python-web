
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRETE_KEY=os.environ.get('SECRETE_KEY') #or 
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	FLASK_ADMIN=os.environ.get('FLASKY_ADMIN')
	
	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	SECRETE_KEY="=\xf1\x87\xe5\x95L\xe5\xe5h\x00E\xebi\xa3\x07\xee\x0b\xb3kn\x86'#\x11"
	DEBUG=True
	SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URI') or 'sqlite:///'+os.path.join(basedir,'db.sqlite')

   
config={
'development':DevelopmentConfig,
'default':DevelopmentConfig
}   	
