#coding=utf-8

from . import BaseHandler


class MemberPageHandler(BaseHandler):
    def get(self, name):
        member = self.get_member(name)
        self.render('member.html', member=member)


class MemberPostsHandler(BaseHandler):
    def get(self, name):
        member = self.get_member(name)
        self.render('member_posts.html', member=member)


class MemberRepliesHandler(BaseHandler):
    def get(self, name):
        member = self.get_member(name)
        self.render('member_replies.html', member=member)


class BlockHandler(BaseHandler):
    def get(self, name):
        pass


class RemoveHandler(BaseHandler):
    def get(self, name):
        member = self.get_member(name)
        member_id = member['_id']
        self.application.db.posts.remove({'author': member_id})
        self.application.db.replies.remove({'author': member_id})
        self.application.db.members.remove({'_id': member_id})


handlers = [
    (r'/member/(\w+)', MemberPageHandler),
    (r'/member/(\w+)/posts', MemberPageHandler),
    (r'/member/(\w+)/replies', MemberRepliesHandler),
    (r'/member/(\w+)/block', BlockHandler),
    (r'/member/(\w+)/remove', RemoveHandler),
]
