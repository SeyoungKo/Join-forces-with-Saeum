package com.conference.assistant.springboot.conferenceassistantspringboot.domain.participant;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.room.Room;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@NoArgsConstructor
public class Participant {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(nullable = false, name="participant_id")
    private Long id;

    // room id
    @ManyToOne
    @JoinColumn(name="room_id")
    private Room room;

    // user id
    @ManyToOne
    @JoinColumn(name="user_id")
    private User user;

    @Column(nullable = false, name="status_participant")
    @Enumerated(EnumType.STRING)
    private Status status;

    @Builder
    public Participant(Room room, User user, Status status) {
        this.room = room;
        this.user = user;
        this.status = status;
    }
}
