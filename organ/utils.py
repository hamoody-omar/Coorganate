
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan, OrganWatched, OrganRequested

def get_filtered_organs(filter_type, id):

        if filter_type == "organ_type":
            persons_organs = PersonOrgan.objects.filter(organ__organ_type=id)
        elif filter_type == "blood_type":
            persons_organs = PersonOrgan.objects.filter(person__blood_type=id)
        else:
            persons_organs = PersonOrgan.objects.all()

        addresses = []
        organizations = []
        requested_organs = []
        watched_organs = []
        used_persons_organs = []

        
        for person_organ in persons_organs:
            try:
                addresses.append(OrganAddress.objects.get(organ=person_organ.organ).address)
                organizations.append(OrganizationOrgan.objects.get(organ=person_organ.organ).organization)

                if OrganRequested.objects.filter(organ=person_organ.organ):
                    if id == "notrequested":
                        addresses.pop()
                        organizations.pop()
                        continue
                    requested_organs.append("Requested")
                else:
                    if id == "requested":
                        addresses.pop()
                        organizations.pop()
                        continue
                    requested_organs.append("Not requested")
                
                if OrganWatched.objects.filter(organ=person_organ.organ):
                    watched_organs.append(OrganWatched.objects.filter(organ=person_organ.organ).count())
                else:
                    watched_organs.append(0)
                used_persons_organs.append(person_organ)
            except:
                continue
        
        return zip(used_persons_organs, addresses, organizations, requested_organs, watched_organs )
