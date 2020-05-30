from jira import JIRA


def login_jira(server ,username ,password):

    jira = JIRA(server = server ,basic_auth =(username ,password))

    return jira

jira = login_jira('https://jira.xforceplus.com','songruimin@xforceplus.com','Srm922819')
print(jira)