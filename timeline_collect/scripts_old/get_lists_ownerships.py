##############################################################################################################
##############################################################################################################
    @property
    def get_lists_ownerships(self):
        """ :reference: https://dev.twitter.com/rest/reference/get/lists/ownerships
            :allowed_param:'screen_name','user_id', 'count', 'cursor'
        """
        return bind_api(
            api=self,
            path='/lists/ownerships.json',
            payload_type='list',
            allowed_param=['screen_name','user_id', 'count', 'cursor',]
        )
##############################################################################################################
##############################################################################################################

