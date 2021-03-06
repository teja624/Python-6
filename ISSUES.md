ISSUES
======

*THE SOFTWARE IS NOT PRODUCTION READY!*

The following list below should not be considered Authoritative.  It is simply
a list of issues that the developers have noticed.  The software is Open Source
so you are free to modify the code.  Those modifications could result in issues
that compromise the software.  You should have a Qualified Engineer go over this
software as well as your changes before deployment.

As of Version 4-Initial the following is a list of known issues:
----------------------------------------------------------------

  *  *OMG UNICODE!!!*  There is no easy way to put this App Engine Python and
     Unicode are not a match made in Heaven.  The db.BlobProperty simply
     screams when fed a Unicode text file.  App Engine Email screams when
     receiving a Unicode Email Header.  Could be others Unicode issues as well.

     *Resolution:*  Still looking into both problems.  I created a hack work
     around for the db.BlobProperty by parsing the string a stripping the
     Unicode.  This works for ASCII text that ends up sent in Unicode, but
     basically wipes out any other langauge special characters especially Asian
     languages.  I am considering the same solution for Email Headers but 1.
     really dislike hacks.  2. we live in a global world, ignoring other cultures
     doesn't work.

  *  *No Page Level Security*, allows users to bypass the verification step and
     still use the service.

     *Resolution:*  This is currently by design.  In version 4 we will be changing
     the models and moving the queries and other data access to the model where
     it belongs.  Security and validation will be part of that migration.

  *  *The software implicitly trusts User Input*, and there is no validation. This
     can lead to malicious content being stored and distributed.  Before using
     this software for public facing applications the user input should be
     validated and cleaned.  

     *Resolution:*  In Version 3 This is mitigated by striping tags on the output,
     and autoescape enabled on the templates.  JavaScript validation and 
     Datastore validation to be added in Version 4.

  *  *The software uses GET/POST methods* which have been shown to be weak to
     Cross Site Request Forgery (CSRF) and code needs to be developed to
     prevent your application from being vulnerable.

     *Resolution:*  Currently the code is vulnerable to CSRF.  This is mitigated
     slightly by only using POST methods for modifing data.  This needs to be
     dealt with before putting the code into production.  Some resources on
     dealing with this are:
     * http://www.codinghorror.com/blog/2008/10/preventing-csrf-and-xsrf-attacks.html
     * http://www.codinghorror.com/blog/2008/09/cross-site-request-forgeries-and-you.html
     * http://freedom-to-tinker.com/sites/default/files/csrf.pdf
     * http://stackoverflow.com/questions/198520/how-to-best-prevent-csrf-attacks-in-a-gae-app
     * http://stackoverflow.com/questions/8384729/is-there-any-available-solution-to-provide-xsrf-csrf-support-for-google-app-engi
     * http://www.pythonsecurity.org/wiki/cross-siterequestforgery/

  *  *Cross Site Scripting* (XSS) As above user input is not filtered thus a
     malicious user could add JavaScript to a Shout that is malicious.  

     *Resolution:*  In Version 3 Shouts have been stripped at display, and all 
     other fields are set to autoescape.

  *  *SQL Injection*, this software uses the App Engine Datastore so most likely
     there is little chance of a SQL Injection like attack, but it might be
     possible with the current code that a malicious user could inject code that
     creates a similar effect by injecting GQL in a returned value.  This is
     limited in that GQL does not support ; so they would be limited to adding
     conditionals.  Also currently none of the queries use user modifiable 
     variables, and all the queries use parameterized queries not string
     concatenation.

     *Resolution:*  SQL Injection type of attacks are of limited use on App Engine
     Datastore.  Provided you do not use string concatenation and only
     parameterized queries you should be safe.  But as always be cautious of how
     you develop the systems that use user input.  Never trust the user.

  *  *No Error Handling*  Currently the software does not contain any error
     handling.  If something causes an error it will not be trapped and the
     software will crash.

     *Resolution:*  This functionality will be developed in version 4 with the
     migration of model code.

  *  *No URL Based OpenID* - OpenID is only functioning on providers who have a
     login page.  Providers whom only authenticate via a URL are currently not
     supported.

     *Resolution:*  Support currently scheduled to be added in version 5

  *  *Favicon not displaying in production.*

     *Resolution:*  Displays in development but not on production.  Probably
     something in app.yaml.  Actually the issue was that all the pages were
     using /static/images/favicon.ico whereas App Engine wanted it to be in
     root /favicon.ico fixed app.yaml to fix this.

This is only a list of known issues.  There could be other issues that have not
been discovered.
