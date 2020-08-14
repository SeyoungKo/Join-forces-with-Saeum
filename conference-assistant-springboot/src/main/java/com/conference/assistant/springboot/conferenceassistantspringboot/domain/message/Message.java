package com.conference.assistant.springboot.conferenceassistantspringboot.domain.message;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.room.Room;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@NoArgsConstructor
@Getter
public class Message {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(nullable = false, name="message_id")
    private Long id;

    @Column(nullable = false)
    private String context;

    // room id 참조
    @ManyToOne
    @JoinColumn(name="room_id")
    private Room room;

    @Builder
    public Message(String context, Room room) {
        this.context = context;
        this.room = room;
    }
}
