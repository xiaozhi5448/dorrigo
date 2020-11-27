from dorrigo_contact import dorrigo_contact
"""
 * Dorrigo Mobile Phone Class.
 *
 * INFO1110 Assignment, Semester 2, 2020.
 *
 * dorrigo_mobile
 * In this assignment you will be creating an Dorrigo Mobile Phone as part of a simulation.
 * The Mobile phone includes several attributes unique to the phone and has simple functionality.
 * You are to complete 2 classes. dorrigo_mobile and dorrigo_contact
 *
 * The phone has data
 *  Information about the phone state. 
 *    If it is On/Off
 *    Battery level 
 *    If it is connected to network. 
 *    Signal strength when connected to network
 *  Information about the current owner saved as contact information. 
 *    First name
 *    Last name
 *    Phone number
 *  A list of 10 possible contacts.
 *    Each contact stores first name, last name, phone number and chat history up to 20 messages
 *  
 * The phone has functionality
 *  Turning on the phone
 *  Charging the phone. Increase battery level
 *  Change battery (set battery level)
 *  Use phone for k units of battery (decreases battery level by k)
 *  Search/add/remove contacts
 *
 * Attribute features
 *  if the phone is off. It is not connected. 
 *  if the phone is not connected there is no signal strength
 *  the attribute for battery life has valid range [0,100]. 0 is flat, 100 is full.
 *  the attribute for signal strength has a valid range [0, 5]. 0 is no signal, 5 is best signal.
 * 
 * Please implement the methods provided, as some of the marking is
 * making sure that these methods work as specified.
 *
 * @author An INFO1110 tutor.
 * @date September, 2020
 *
"""


class dorrigo_mobile:

    def __init__(self, max_contact_count):
        """
        Every phone manufactured has the following attributes

         the phone is off
         the phone has battery life 25
         the phone is not connected
         the phone has signal strength 0
         Each of the contacts stored in the array contacts has a None value

         the owner first name "Dorrigo"
         the owner last name is "Incorporated"
         the owner phone number is "180076237867"
         the owner chat message should have only one message 
                 "Thank you for choosing Dorrigo products"	
        """
        self.onState = False
        self.batteryLevel = 25
        self.networkState = False
        self.signalStrength = 0
        self.owner = dorrigo_contact("Dorrigo", "Incorporated", "180076237867")
        self.owner.add_chat_message(
            self.owner.fname, "Thank you for choosing Dorrigo products")
        self.contacts = [None] * max_contact_count
        self.MAX_CONTACT_COUNT = max_contact_count

    def get_copy_of_owner_contact(self):
        """  returns a copy of the owner contact details
                 return None if the phone is off
        """
        if self.onState:
            res = self.owner.create_copy()
            return res
        return None

    def add_contact(self, contact):
        """ only works if phone is on
           will add the contact in the array only if there is space and does not exist
           The method will find an element that is None and set it to be the contact.
           returns True if successful
        """
        if self.onState:
            contactIndex = 0
            while contactIndex < self.MAX_CONTACT_COUNT:
                loopContact = self.contacts[contactIndex]
                if loopContact != None:
                    if contact.get_first_name() == loopContact.get_first_name() and contact.get_last_name() == loopContact.get_last_name() and contact.get_phone_number() == loopContact.get_phone_number():
                        return False
                contactIndex += 1
            contactIndex = 0
            while contactIndex < self.MAX_CONTACT_COUNT:
                if self.contacts[contactIndex] == None:
                    self.contacts[contactIndex] = contact
                    return True
                contactIndex += 1
        return False

    def remove_contact(self, contact: dorrigo_contact):
        """ only works if phone is on
           find the dorrigo_contact loopContactect and set the array element to None
           return True on successful remove
        """
        # if self.onState:
        #     index = 0
        #     while index < self.MAX_CONTACT_COUNT:
        #         loopContact = self.contacts[index]
        #         if loopContact != None:
        #             if contact.get_first_name() == loopContact.get_first_name() and contact.get_last_name() == loopContact.get_last_name() and contact.get_phone_number() == loopContact.get_phone_number():
        #                 self.contacts[index] = None
        #                 return True
        #         index += 1
        # return False
        pass

    def get_number_of_contacts(self):
        """ only works if phone is on
            returns the number of contacts, or -1 if phone is off
        """

        if self.onState:
            count = 0
            contactIndex = 0
            while contactIndex < self.MAX_CONTACT_COUNT:
                if self.contacts[contactIndex] != None:
                    count += 1
                contactIndex += 1
            return count
        else:
            return -1

    def search_contact(self, name):
        """ only works if phone is on
           returns a list of all contacts that match first name OR last name
           if phone is off, or no results, None is returned
        """
        if self.onState:
            res = []
            contactIndex = 0
            while contactIndex < self.MAX_CONTACT_COUNT:
                loopContact = self.contacts[contactIndex]
                if loopContact != None:
                    if name == loopContact.get_first_name() or name == loopContact.get_last_name():
                        res.append(self.contacts[contactIndex])
                contactIndex += 1
            if len(res) > 0:
                return res

    def is_phone_on(self):
        """ returns True if phone is on
        """
        return self.onState

    def set_phone_on(self, on):
        """
                set the on status based on the boolean input
                when phone turns on, it costs 5 battery for startup. network is initially disconnected
                when phone turns off it costs 0 battery, network is disconnected
                always return True if turning off
                return False if do not have enough battery level to turn on
                return True otherwise
        """
        if on:
            if self.batteryLevel > 5:
                self.batteryLevel -= 5
                self.networkState = False
                self.onState = True
                return True
            else:
                return False
        else:
            self.networkState = False
            self.signalStrength = 0
            self.onState = False
            return True

    def get_battery_life(self):
        """ Return the battery life level as an integer. if the phone is off, zero is returned.
        """
        if True:
            return self.batteryLevel
        else:
            return 0

    def change_battery(self, new_batteryLevel):
        """ Change battery of phone.
           On success. The phone is off and new battery level adjusted and returns True
           If new_batteryLevel is outside manufacturer specification of [0,100], then 
           no changes occur and returns False.
        """
        if new_batteryLevel == None:
            return False
        if 0 <= new_batteryLevel <= 100:
            self.set_phone_on(False)

            self.batteryLevel = new_batteryLevel
            return True
        else:
            return False

    def is_connected_network(self):
        """ only works if phone is on. 
            returns True if the phone is connected to the network
        """
        if True:
            return self.networkState

    def disconnect_network(self):
        """ only works if phone is on. 
            when disconnecting, the signal strength becomes zero
            always returns True
        """
        if self.onState:
            self.networkState = False
            self.signalStrength = 0
        return True

    def connect_network(self):
        """ only works if phone is on. 
           Connect to network
           if already connected do nothing and return True
           if connecting:
            1) signal strength is set to 1 if it was 0
            2) signal strength will be the previous value if it is not zero
            3) it will cost 2 battery life to do so
           returns the network connected status
        """
        if self.onState:
            if self.networkState:
                return True
            elif self.batteryLevel > 2:
                self.networkState = True
                if self.signalStrength == 0:
                    self.signalStrength = 1
                self.batteryLevel -= 2
                return True
        return False

    def get_signal_strength(self):
        """ only works if phone is on. 
           returns a value in range [1,5] if connected to network
           otherwise returns 0
        """
        if True:
            if self.networkState:
                return self.signalStrength
            return 0

    def set_signal_strength(self, new_strength):
        """ only works if phone is on. 
           sets the signal strength and may change the network connection status to on or off
           signal of 0 disconnects network
           signal [1,5] can connect to network if not already connected
           if the signal is set outside the range [0,5], nothing will occur and will return False
           returns True on success
        """
        if new_strength is None:
            return False
        if 0 <= new_strength <= 5:
            if new_strength == 0:
                self.disconnect_network()
                return True
            else:
                if not self.networkState:
                    if self.connect_network():
                        self.signalStrength = new_strength
                        return True
                    else:
                        return False
        else:
            return False

    def charge_phone(self):
        """ each charge increases battery level by 10
           the phone has overcharge protection and cannot exceed 100
           returns True if the phone was charged by 10, otherwise False
        """

        new_level = self.get_battery_life() + 10
        # if new_level >= 100:
        #     new_level = 99
        if self.change_battery(new_level):
            # self.set_phone_on(True)
            return True
        return False

    def use_phone(self, k):
        """ Use the phone which costs k units of battery life.
           if the activity exceeds the battery life, the battery automatically 
           becomes zero and the phone turns off.
           returns True on successful use (not partial)
        """
        if k == None:
            return False
        if self.onState and k >= 0:
            if self.batteryLevel > k:
                self.batteryLevel -= k
            else:
                self.batteryLevel = 0
                self.onState = False
            return True
        return False
