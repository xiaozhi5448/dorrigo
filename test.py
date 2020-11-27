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

from dorrigo_contact import dorrigo_contact


class dorrigo_mobile:

    def __init__(self, max_contacts):
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
        self.phoneOff = True
        self.batteryLife = 25
        self.connectPhone = False
        self.signalStrength = 0
        self.contacts = [None]*max_contacts
        self.owner = dorrigo_contact("Dorrigo", "Incorporated", "180076237867")
        self.owner.add_chat_message(
            self.owner.fname, "Thank you for choosing Dorrigo products")

    def get_copy_of_owner_contact(self):
        """  returns a copy of the owner contact details
               return None if the phone is off
        """
        if self.phoneOff is False:
            Huawei = dorrigo_contact(
                self.owner.fname, self.owner.name, self.owner.pnumber)
            Huawei.add_chat_message(
                self.owner.fname, 'Thank you for choosing Dorrigo products')
            return Huawei
        else:
            return None

    def add_contact(self, contact):
        """ only works if phone is on
           will add the contact in the array only if there is space and does not exist
           The method will find an element that is None and set it to be the contact.
           returns True if successful
        """
        def find_way(location, count, contacts):
            if count > 0:
                if contacts[count-1] and contacts[count-1].fname == contacts.fname and \
                        contact[count-1].lname == contact.lname:
                    return-1
                if contacts[count-1] is None:
                    location = count-1
                return find_way(location, count-1, contacts)
            else:
                return location

        if self.phoneOff is False:
            loca = find_way(len(self.contactsArry), self.contactsArry)
            if loca == -1:
                return False
            else:
                self.contactsArry[loca] = contact
                return True
        else:
            return False

    def remove_contact(self, contact):
        """ only works if phone is on
           find the dorrigo_contact object and set the array element to None
            return True on successful remove
        """
        def find_way(location, count, contacts):
            if count > 0:
                if contacts[count-1] and contacts[count-1].fname == contact.fname and \
                        contacts[count-1].lname == contact.lname:
                    return cnt-1
                return find_way(location, count-1, contacts)
            else:
                return location
        if self.phoneOff is False:
            loca = find_way(-1, len(self.contactsArray), self.contactsArray)
            if loca == -1:
                return False
            else:
                self.contactsArray[loca] = None
                return True
        else:
            return False

    def get_number_of_contacts(self):
        """ only works if phone is on
            returns the number of contacts, or -1 if phone is off
        """
        if self.on:
            count = 0
            index = 0
            while index < len(self.contacts):
                if self.contacts[index] != None:
                    count += 1
                index += 1
            return count
        else:
            return -1

    def search_contact(self, name):
        """ only works if phone is on
           returns a list of all contacts that match first name OR last name
           if phone is off, or no results, None is returned
        """
        if not self.phoneOff:
            res = []
            index = 0
            while index < len(self.contacts):
                obj = self.contacts[index]
                if obj != None:
                    if name == obj.get_first_name() or name == obj.get_last_name():
                        res.append(self.contacts[index])
                index += 1
            if len(res) > 0:
                return res

    def is_phone_on(self):
        """ returns True if phone is on
        """
        if self.phoneOff == False:
            return True
        else:
            return False

    def set_phone_on(self, on):
        """
            set the on status based on the boolean input
            when phone turns on, it costs 5 battery for startup. network is initially disconnected
            when phone turns off it costs 0 battery, network is disconnected
            always return True if turning off
            return False if do not have enough battery level to turn on
            return True otherwise
        """
        if on is True:
            if self.phoneOff is False:
                return True
            else:
                if self.batteryLife <= 5:
                    return False
                else:
                    self.batteryLife = self.batteryLife-5
                    self.connectPhone = False
                    self.phoneOff = False
                    return True
        else:
            self.phoneOff = True
            self.connectPhone = False
            return True

    def get_battery_life(self):
        """ Return the battery life level as an integer. if the phone is off, zero is returned.
        """
        if self.phoneOff is False:
            return int(self.batteryLife)
        else:
            return 0

    def change_battery(self, new_battery_level):
        """ Change battery of phone.
           On success. The phone is off and new battery level adjusted and returns True
           If new_battery_level is outside manufacturer specification of [0,100], then 
           no changes occur and returns False.
        """
        if 0 < new_battery_level < 100:
            self.phoneOff = True
            self.batteryLife = new_battery_level
            return True
        else:
            return False

    def is_connected_network(self):
        """ only works if phone is on. 
            returns True if the phone is connected to the network
        """
        if self.phoneOff == False:
            if self.connectPhone:
                return True
            else:
                return False
        else:
            return False

    def disconnect_network(self):
        """ only works if phone is on. 
            when disconnecting, the signal strength becomes zero
            always returns True
        """
        if self.phoneOff == False:
            self.connectPhone = False
            self.signalStrength = 0
            return True
        else:
            return False

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
        if self.phoneOff is False:
            if self.connectPhone:
                return True
            else:
                if self.signalStrength == 0:
                    self.signalStrength = 1
                    self.connectPhone = True
                if self.batteryLife > 2:
                    self.batteryLife = self.batteryLife-2
                    self.connectPhone = True
                else:
                    self.batteryLife = 0
                    self.disconnect_network()
                    return False
                return self.connectPhone
        else:
            return False

    def get_signal_strength(self):
        """ only works if phone is on. 
           returns a value in range [1,5] if connected to network
           otherwise returns 0
        """
        if self.phoneOff is False:
            if self.connectPhone and 1 <= self.signalStrength <= 5:
                return True
            else:
                return None
        else:
            return None

    def set_signal_strength(self, new_strength):
        """ only works if phone is on. 
           sets the signal strength and may change the network connection status to on or off
           signal of 0 disconnects network
           signal [1,5] can connect to network if not already connected
           if the signal is set outside the range [0,5], nothing will occur and will return False
           returns True on success
        """
        if self.phoneOff is False:
            if new_strength < 0 or new_strength > 5:
                return False
            else:
                if new_strength == 0:
                    self.signalStrength = new_strength
                    self.connectPhone = False
                else:
                    self.signalStrength = new_strength
                    self.connectPhone = True
                return True
        else:
            return False

    def charge_phone(self):
        """ each charge increases battery level by 10
           the phone has overcharge protection and cannot exceed 100
           returns True if the phone was charged by 10, otherwise False
        """
        pass

    def use_phone(self, k):
        """ Use the phone which costs k units of battery life.
           if the activity exceeds the battery life, the battery automatically 
           becomes zero and the phone turns off.
           returns True on successful use (not partial)
        """
        pass
