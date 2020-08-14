package com.conference.assistant.springboot.conferenceassistantspringboot.domain.participant;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.room.Room;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.User;
import lombok.Builder;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@NoArgsConstructor
public class Participant {

    // room id
    @ManyToOne
    @JoinColumn(name="room_id")
    private Room room;

    // user id
    @ManyToOne
    @JoinColumn(name="user_id")
    private User user;

    @Column(nullable = false)
    @Enumerated(EnumType.STRING)
    private Status_p status_p;

    @Builder
    public Participant(Room room, User user, Status_p status_p) {
        this.room = room;
        this.user = user;
        this.status_p = status_p;
    }
}
